import feedparser
import html2text
import os, json
from datetime import timezone, datetime
import dateparser


class RSS:
    title: str
    summary: str
    link: str
    date: str
    info: dict

    def __init__(self, title, summary, link, date, info):
        self.title = title
        self.summary = summary
        self.link = link
        self.date = date
        self.info = info


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

    for article in res[keymap["items"]]:

        title = article["title"]

        html_transform = html2text.HTML2Text()
        html_transform.ignore_links = True
        html_transform.ignore_images = True
        html_transform.ignore_tables = True
        html_transform.ignore_emphasis = True

        summary = html_transform.handle(article["summary"])
        link = article["link"]
        article_date = unify_timezone(article[keymap["date"]])
        rss = RSS(title, summary, link, article_date.strftime("%Y-%m-%d %H:%M:%S"), res[keymap["channel"]])
        if article_date.date() == datetime.today().date():
            # 判断是否当天信息
            return rss
    return None


def unify_timezone(date_string):
    str_date = dateparser.parse(date_string,
                                settings={"TIMEZONE": "Asia/Shanghai",
                                          "RETURN_AS_TIMEZONE_AWARE": True})
    return str_date
