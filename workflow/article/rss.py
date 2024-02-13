import feedparser
import html2text
import os, json, re
from datetime import datetime
import dateparser
import requests
from bs4 import BeautifulSoup


class RSS:
    title: str
    summary: str
    link: str
    date: str
    info: dict
    type: str

    def __init__(self, title, summary, link, date, info, type_name):
        self.title = title
        self.summary = summary
        self.link = link
        self.date = date
        self.info = info
        self.type = type_name


def load_rss_configs():
    # 获取当前文件的所在目录
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # 获取当前项目的根目录
    project_root = os.path.dirname(current_directory)

    rss_folder = project_root + "/resources"

    rss_configs = []
    rss_items = []

    for file in os.listdir(rss_folder):
        print(file)
        with open(os.path.join(rss_folder, file), "r") as fp:
            data = json.loads(fp.read())
            rss_configs.extend(data)

    for rss_category in rss_configs:
        for rss in rss_category["items"]:
            rss_items.append(rss)

    return rss_items


def parse_rss_item(rss_item):
    """仅获取当天的rss信息"""
    res = feedparser.parse(rss_item["url"])
    keymap = res.keymap

    today_rss = []

    for article in res[keymap["items"]]:
        title = article["title"]
        link = article["link"]
        if rss_item.get("type") == "link":
            summary = parse_web_page(url=link)
        elif rss_item.get("type") == "image":
            summary = transform_html2txt(article["summary"], False)
        else:
            summary = transform_html2txt(article["summary"])
        article_date = unify_timezone(article.get(keymap["date"], res.get(keymap["date"])))
        rss = RSS(title,
                  summary,
                  link,
                  article_date.strftime("%Y-%m-%d %H:%M:%S"),
                  res[keymap["channel"]],
                  rss_item.get("type", "default"))
        if article_date.date() == datetime.today().date():
            # 判断是否为当天信息，可能有多个内容
            today_rss.append(rss)
    # 防止一个地址有过多内容，这里限定下数量
    return today_rss[:3]


def transform_html2txt(content, ignore_image=True):
    html_transform = html2text.HTML2Text()
    html_transform.ignore_links = True
    html_transform.ignore_images = ignore_image
    html_transform.ignore_tables = True
    html_transform.ignore_emphasis = True
    text = html_transform.handle(content)
    if not ignore_image:
        return extract_image_links(text)
    return text


def unify_timezone(date_string):
    str_date = dateparser.parse(date_string,
                                settings={"TIMEZONE": "Asia/Shanghai",
                                          "RETURN_AS_TIMEZONE_AWARE": True})
    return str_date


def parse_web_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # 使用BeautifulSoup解析HTML
            soup = BeautifulSoup(response.text.encode("utf-8"), 'html.parser')

            # 提取限定标签
            paragraphs = soup.find_all(["h1", "h2", "p"])
            paragraphs_text = [p.get_text() for p in paragraphs]
            extracted_text = '\n'.join(paragraphs_text)
            return extracted_text.strip()
        else:
            print(f"Failed to retrieve webpage. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None


def extract_image_links(text):
    # 定义匹配Markdown格式图片链接的正则表达式
    image_link_regex = r"!\[[^\]]*\]\((.*?)\)"
    image_links = re.findall(image_link_regex, text)
    return "".join(image_links[:1])
