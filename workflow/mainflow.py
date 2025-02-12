import os, json, datetime, glob

from workflow.article.rss import Article
from workflow.gpt.summary import evaluate_article_with_gpt
import workflow.article.rss as rss
import workflow.article.blog as blog
import time

from loguru import logger


def execute(rss_resource="workflow/resources"):
    # 缓存判断
    cache_folder, cache_file = find_valid_file()
    origin_article_list = parse_daily_rss_article(rss_resource, cache_file)
    if cache_folder:
        save_article(origin_article_list, cache_folder)
    articles = find_favorite_article(origin_article_list)
    blog.make_daily_markdown_with(articles, origin_article_list)


def parse_daily_rss_article(rss_resource, cache_file=None):
    """获取rss信息"""
    if cache_file:
        return decode_article(cache_file)
    rss_items = rss.load_rss_configs(rss_resource)

    telegram_prefix = "https://t.me/"

    daily_rss = []
    for item in rss_items:
        rss_list = rss.parse_rss_config(item)
        for rss_item in rss_list:
            daily_rss.append(rss_item)
            if rss_item.link.startswith(telegram_prefix):
                rss_item = rss.transform_telegram_article(rss_item)
            logger.info(f"date: {rss_item.date}, link: {rss_item.link}")
    return daily_rss


def find_favorite_article(rss_articles):
    """获取评分最高的文章"""
    # 限流，文章最多分析20篇
    max_analyze_nums = 60
    rss_articles = rss_articles[:max_analyze_nums]
    # 默认输出结果10
    max_article_nums = int(os.environ.get("MAX_ARTICLE_NUMS", "12"))
    # 一个rss源对应一个总结，多条内容，合并处理
    # {"Apple News": [<article>]}
    rss_resource = {}
    for article in rss_articles:
        if not article.summary:
            continue
        rss_category = article.info["title"]
        if rss_category in rss_resource.keys():
            rss_resource[rss_category].append(article)
        else:
            rss_resource[rss_category] = [article]

    show_articles = []
    for key, articles in rss_resource.items():
        # 防止 gemini 限频
        time.sleep(2)
        evaluate_results = evaluate_article_with_gpt(articles)
        for evaluate in evaluate_results:
            for article in articles:
                if article.link == evaluate.get("link"):
                    article.evaluate = evaluate

        # 有可能某些内容未总结完成，过滤
        articles = [item for item in articles if item.evaluate and item.evaluate.get("score")]
        if not articles:
            continue

        articles.sort(key=lambda x: x.evaluate["score"], reverse=True)
        logger.info(f"count: {len(articles)}")
        # 满分内容，可展示多个
        full_score_evaluates = [item for item in articles if item.evaluate["score"] >= 10]
        # 默认输出数量 1
        output_count = articles[0].config.get("output_count", 2)
        logger.info(f"expect max count: {output_count}")
        if len(full_score_evaluates) >= output_count:
            select_articles = full_score_evaluates
        else:
            select_articles = articles[:output_count] if len(articles) >= output_count else articles
        show_articles.extend(select_articles)
        logger.info(f"select articles: {[item.title for item in select_articles]}")
    # 汇总之后再排序
    show_articles.sort(key=lambda x: x.evaluate["score"], reverse=True)
    return show_articles[:max_article_nums]


def find_valid_file():
    """是否为有效rss缓存"""
    if os.environ.get("RSS_CACHE_ENABLE") != "true":
        return None, None

    current_directory = os.path.dirname(os.path.abspath(__file__))

    cache_folder = f"{current_directory}/draft"
    today_str = datetime.date.today().strftime('%Y-%m-%d')
    cache_files = glob.glob(f"{cache_folder}/*{today_str}.json")
    cache_file = cache_files[-1] if cache_files else None
    return cache_folder, cache_file


def save_article(articles, draft_folder):
    """存储解析的文章"""
    data = []
    path = f"{draft_folder}/article_cache_{datetime.date.today().strftime('%Y-%m-%d')}.json"
    for article in articles:
        data.append(article.__dict__)

    with open(path, "w") as fp:
        fp.write(json.dumps(data, indent=4))


def decode_article(path):
    """根据文件解析"""
    rss_list = []
    with open(path, "r") as fp:
        object_list = json.loads(fp.read())
        for item in object_list:
            rss_item = rss.Article()
            for key, value in item.items():
                setattr(rss_item, key, value)
            rss_list.append(rss_item)
    return rss_list
