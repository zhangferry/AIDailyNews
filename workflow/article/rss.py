import feedparser
import html2text
import os, json, re, time
from datetime import datetime, timedelta
from dateutil import tz
import dateparser
import requests
from bs4 import BeautifulSoup
from loguru import logger
from markdown import markdown

# 统一时区
time_zone_value = "Asia/Shanghai"

# 创建全局 HTTP Session 以复用连接
_http_session = requests.Session()
# 配置连接池和重试
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
)
adapter = HTTPAdapter(max_retries=retry_strategy, pool_connections=10, pool_maxsize=20)
_http_session.mount("http://", adapter)
_http_session.mount("https://", adapter)


class Article:
    title: str
    summary: str
    link: str
    cover_url: str  # 封面链接
    date: str
    info: dict
    # rss 配置信息
    config: dict
    evaluate: dict = None  # 来源于ai生成

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @staticmethod
    def make_with_dict(obj_dict):
        rss = Article()
        for key, value in obj_dict.items():
            setattr(rss, key, value)
        return rss


def load_rss_configs(resource):
    rss_configs = {}
    rss_categories = []
    rss_items = []

    def load_config_with(path):
        with open(path, "r") as fp:
            data = json.loads(fp.read())
            rss_categories.extend(data["categories"])
            rss_configs.update(data["configuration"])

    if os.path.isdir(resource):
        for file in os.listdir(resource):
            if file.endswith("json"):
                load_config_with(os.path.join(resource, file))
    else:
        load_config_with(resource)

    for rss_category in rss_categories:
        for rss in rss_category["items"]:
            rss["category"] = rss_category.get("category", "Daily News")
            if "rsshub_path" in rss:
                rss["url"] = rss_configs["rsshub_domain"] + rss["rsshub_path"]
            rss_items.append(rss)

    return rss_items


def parse_rss_config(rss_config):
    """仅获取当天的rss信息"""
    res = feedparser.parse(rss_config["url"],
                           agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
    keymap = res.keymap
    today_rss = []
    # 默认一个rss源只获取一定数量信息
    max_count = rss_config.get("input_count", 4)

    for article in res[keymap["items"]]:
        # 获取当天信息
        time_zone = tz.gettz(time_zone_value)
        target_date = datetime.today().astimezone(time_zone).date()
        # issued > date > res.date
        article_date = unify_timezone(article.get(keymap["issued"],
                                                  article.get(keymap["date"],
                                                              res.get(keymap["date"]))))
        if not article_date or article_date.date() != target_date:
            continue
        rss = gen_article_from(rss_item=article, rss_type=rss_config.get("type"), image_enable=rss_config.get("image_enable", False),
                               rss_date=article_date.strftime("%Y-%m-%d %H:%M:%S"), channel=res[keymap["channel"]],
                               config=rss_config)
        if rss is None:
            continue
        today_rss.append(rss)
        if len(today_rss) >= max_count:
            return today_rss
    # 防止一个地址有过多内容，这里限定下数量
    if len(today_rss) == 0:
        logger.info(f'{rss_config["url"]} content of today is empty')
    else:
        logger.info(f'{rss_config["url"]} content count of today is {len(today_rss)}')
    return today_rss

def gen_article_from(rss_item, rss_type, image_enable=False, rss_date=None, channel=None, config=None):
    title = rss_item["title"]
    link = rss_item["link"]
    summary_raw = rss_item.get("summary", "")
    image_url = ""

    if rss_type and len(rss_type) != 0:
        summary, fetched_image = fetch_summary_from(url=link, rss_type=rss_type)
        if fetched_image:
            image_url = fetched_image
    else:
        summary, image_url = transform_html2txt(summary_raw, image_enable=image_enable)

    if not summary or len(summary) < 10:
        return None

    # If no image found, try fetching from the article URL
    if not image_url and link:
        image_url = fetch_cover_image_from_url(link)

    article = Article(title=title,
                  summary=summary,
                  link=link,
                  date=rss_date,
                  info=channel,
                  config=config,
                  cover_url=image_url)
    return article

def fetch_summary_from(url: str, rss_type: str):
    summary = None
    image_url = ""
    if rss_type == "link":
        summary, image_url = parse_web_page(url=url)
    elif rss_type == "code":
        summary = parse_github_readme(url)
        image_url = fetch_github_repo_image(url)
    return summary, image_url


def _is_generated_social_image(url):
    """判断是否为自动生成的社交分享卡片图（非真实文章配图）"""
    generated_patterns = [
        "opengraph-image", "twitter-image", "og-image",
        "/og_", "/social_", "/share-image", "/card-image",
        "metatags", "/meta-image",
    ]
    url_lower = url.lower()
    return any(p in url_lower for p in generated_patterns)


def _find_real_image_in_body(soup, base_url=""):
    """从文章正文中提取第一张有意义的真实图片"""
    # 在常见文章容器中查找
    article = (
        soup.find("article")
        or soup.find("main")
        or soup.find(class_=re.compile(r"article|post|content|entry", re.I))
        or soup.find("body")
    )
    if not article:
        return ""

    skip_keywords = [
        "icon", "logo", "avatar", "badge", "emoji", "pixel",
        "spinner", "loading", "favicon", "touch-icon",
        "apple-touch", "placeholder", "1x1", "blank", "spacer",
        "assets/images/logo", "githubassets.com/assets/github-logo",
        "ad", "banner", "sponsor", "gravatar", "analytics",
        "opengraph-image", "twitter-image",
    ]

    for img in article.find_all("img"):
        src = img.get("src") or img.get("data-src", "")
        if not src or src.startswith("data:") or src.endswith(".svg"):
            continue
        src_lower = src.lower()
        if any(skip in src_lower for skip in skip_keywords):
            continue
        # 过滤过小的图片（宽度属性 < 100 的通常是图标）
        width = img.get("width", "")
        if width and width.isdigit() and int(width) < 100:
            continue
        # 解析相对路径
        if src.startswith("/"):
            from urllib.parse import urljoin
            src = urljoin(base_url, src)
        return src
    return ""


def fetch_cover_image_from_url(url, timeout=10):
    """封面图抓取策略：正文真实图片优先，og:image 兜底，过滤生成的社交卡片"""
    try:
        response = _http_session.get(url, timeout=timeout)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, 'html.parser')

        # 策略1：从文章正文提取真实图片（优先）
        real_image = _find_real_image_in_body(soup, base_url=url)
        if real_image:
            return real_image

        # 策略2：og:image（仅当非自动生成卡片时使用）
        og_image = soup.find("meta", property="og:image")
        if og_image and og_image.get("content"):
            candidate = og_image["content"]
            if not _is_generated_social_image(candidate):
                if not any(skip in candidate.lower() for skip in [
                    "touch-icon", "favicon", "logo", "icon-", "apple-touch",
                ]):
                    if candidate.startswith("/"):
                        from urllib.parse import urljoin
                        candidate = urljoin(url, candidate)
                    return candidate

        # 策略3：twitter:image（仅当非自动生成卡片时使用）
        tw_image = soup.find("meta", attrs={"name": "twitter:image"})
        if tw_image and tw_image.get("content"):
            candidate = tw_image["content"]
            if not _is_generated_social_image(candidate):
                return candidate

        return ""
    except Exception:
        return ""


def transform_telegram_article(article: Article):
    """
    example:
    link: https://t.me/CocoaDevBlogs/22734, summary: Late Night Silent Completions: Jiiiii — Part 446 https://t.co/iXZYsZO0A7
    """
    lines = article.summary.split('\n')
    tco_links = []
    for line in lines:
        if not line.startswith('>'):
            # 使用正则表达式查找以https://t.co开头的链接
            links = re.findall(r'https://t.co\S+', line)
            tco_links.extend(links)
    if len(tco_links) > 0:
        link = get_real_url(tco_links[0])
        article.link = link
        if link.startswith("https://github.com"):
            article.summary, _ = fetch_summary_from(url=link, rss_type="code")
        else:
            article.summary, _ = fetch_summary_from(url=link, rss_type="link")
    return article


def transform_html2txt(content, image_enable=False):
    html_transform = html2text.HTML2Text(bodywidth=0)
    html_transform.ignore_links = True
    html_transform.ignore_images = not image_enable
    html_transform.ignore_tables = True
    html_transform.ignore_emphasis = True
    text = html_transform.handle(content)
    image_url = ""
    if image_enable:
        name, image_url = extract_image_links(text)
    return text, image_url


def unify_timezone(date_string):
    str_date = dateparser.parse(date_string,
                                settings={"TIMEZONE": time_zone_value,
                                          "RETURN_AS_TIMEZONE_AWARE": True})
    return str_date


def parse_web_page(url, timeout=15):
    """解析网页内容，提取正文和首图。正文真实图片优先，og:image 仅作兜底。"""
    try:
        response = _http_session.get(url, timeout=timeout)
        response.raise_for_status()

        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, 'html.parser')

        # 策略1：从文章正文提取真实图片（优先）
        image_url = _find_real_image_in_body(soup, base_url=url)

        # 策略2：og:image（仅当正文无图且非生成卡片时使用）
        if not image_url:
            og_image = soup.find("meta", property="og:image")
            if og_image and og_image.get("content"):
                candidate = og_image["content"]
                if not _is_generated_social_image(candidate) and not any(skip in candidate.lower() for skip in [
                    "touch-icon", "favicon", "logo", "icon-", "apple-touch",
                ]):
                    if candidate.startswith("/"):
                        from urllib.parse import urljoin
                        candidate = urljoin(url, candidate)
                    image_url = candidate

        # 策略3：twitter:image（仅当非生成卡片时使用）
        if not image_url:
            tw_image = soup.find("meta", attrs={"name": "twitter:image"})
            if tw_image and tw_image.get("content"):
                candidate = tw_image["content"]
                if not _is_generated_social_image(candidate):
                    image_url = candidate

        # Extract text content
        tags = soup.find_all(["h1", "h2", "p", "code"])
        tags_text = [tag.get_text() for tag in tags if not tag.next.name]
        extracted_text = '\n'.join(tags_text)

        return extracted_text.strip(), image_url
    except requests.exceptions.Timeout:
        logger.error(f"请求超时: {url}")
        return None, ""
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP 错误: {url}, 状态码: {e.response.status_code}")
        return None, ""
    except requests.exceptions.RequestException as e:
        logger.exception(f"解析网页失败: {url}, 错误: {e}")
        return None, ""


def extract_image_links(text):
    # 定义匹配Markdown格式图片链接的正则表达式，输出为元组格式
    image_link_regex = r"!\[(.*?)\]\((.*?)\)"
    image_links = re.findall(image_link_regex, text)
    if image_links:
        return image_links[0]
    return "", ""


def fetch_github_repo_image(repo_url):
    """获取 GitHub 仓库的社交预览图"""
    try:
        repo_url = get_real_url(repo_url)
        username, repo_name = repo_url.split("/")[-2:]
        api_url = f"https://api.github.com/repos/{username}/{repo_name}"
        headers = {"Accept": "application/vnd.github.v3+json"}
        github_token = ""
        if os.environ.get("GITHUB_ACCESS_TOKEN"):
            github_token = f"token {os.environ.get('GITHUB_ACCESS_TOKEN')}"
        elif os.environ.get("ACCESS_TOKEN"):
            github_token = f"token {os.environ.get('ACCESS_TOKEN')}"
        headers["Authorization"] = github_token
        response = _http_session.get(api_url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        # social_preview_image is the custom repo social image
        image_url = data.get("social_preview_image_url", "")
        if not image_url:
            # Fallback: owner avatar
            image_url = data.get("owner", {}).get("avatar_url", "")
        return image_url
    except Exception as e:
        logger.warning(f"获取仓库图片失败: {repo_url}, 错误: {e}")
        return ""


def parse_github_readme(repo_url):
    try:
        repo_url = get_real_url(repo_url)
        # 提取用户名和仓库名
        username, repo_name = repo_url.split("/")[-2:]
        api_url = f"https://api.github.com/repos/{username}/{repo_name}/readme"
        headers = {
            "Accept": "application/vnd.github.v3+json"
        }

        github_token = ""
        if os.environ.get("GITHUB_ACCESS_TOKEN"):
            github_token = f"token {os.environ.get('GITHUB_ACCESS_TOKEN')}"
        elif os.environ.get("ACCESS_TOKEN"):
            github_token = f"token {os.environ.get('ACCESS_TOKEN')}"
        headers["Authorization"] = github_token
        response = _http_session.get(api_url, headers=headers)
        response.raise_for_status()
        # 解析响应，提取 README 内容
        readme_content = response.json()["content"]
        # 将 Base64 编码的内容解码为字符串
        import base64
        readme_content = base64.b64decode(readme_content).decode("utf-8")

        # md > html > text
        html = markdown(readme_content)
        # remove code snippets
        html = re.sub(r'<pre>(.*?)</pre>', '', html, flags=re.DOTALL)
        html = re.sub(r'<code>(.*?)</code>', '', html, flags=re.DOTALL)
        html = re.sub(r'```(.*?)```', '', html, flags=re.DOTALL)
        soup = BeautifulSoup(html, "html.parser")
        text = ''.join(soup.findAll(string=True))
        return text.strip()

    except Exception as e:
        logger.error(f"fetch {repo_url} get error: {e}")
        return None

def get_real_url(short_url, timeout=10, max_retries=3):
    """获取短链接的真实 URL，支持超时和重试机制"""
    for attempt in range(max_retries):
        try:
            response = _http_session.head(short_url, allow_redirects=True, timeout=timeout)
            response.raise_for_status()
            return response.url
        except requests.exceptions.Timeout:
            logger.warning(f"获取真实 URL 超时 (尝试 {attempt + 1}/{max_retries}): {short_url}")
            if attempt < max_retries - 1:
                time.sleep(1)  # 重试前等待
        except requests.exceptions.RequestException as e:
            logger.error(f"获取真实 URL 失败: {short_url}, 错误: {e}")
            if attempt < max_retries - 1:
                time.sleep(1)
            else:
                return short_url  # 重试失败，返回原始 URL
    return short_url

def rss_env():
    os.environ[""] = ""