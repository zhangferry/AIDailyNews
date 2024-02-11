import datetime

from workflow.mainflow import parse_daily_rss_article
import os
from urllib.parse import urlparse

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # load_rss_resources()

    os.environ["https_proxy"] = "http://127.0.0.1:465"
    os.environ["http_proxy"] = "http://127.0.0.1:465"
    os.environ["all_proxy"] = "http://127.0.0.1:465"

    header = f"""
    ---
    title: {datetime.datetime}
    date: {rss.date}
    author: {url_info.hostname}
    tags: 
    -  {rss.info["title"]}
    ---
    """

    articles = parse_daily_rss_article()
    for article in articles:
        markdown_content = ""
        rss = article["rss"]
        print(rss.title)
        print(rss.link)
        url_info = urlparse(rss.link)
        print(article["score"])
        print(article["summary"])
        print("=====")


