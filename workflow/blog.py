import json, datetime
from urllib.parse import urlparse


def make_markdown_with(articles):
    header = f"""
        ---
        title: "标题"
        date: {datetime.date.today().strftime("%Y-%m-%d %H:%M:%S")}
        author: AI
        tags: 
        -  iOS
        ---
        """
    markdown_content = header
    for article in articles:
        rss = article["rss"]
        article_intro = f"""
        
        ## [{rss.title}]({rss.link})
        {article["summary"]}
        """
        markdown_content += article_intro

        with open("", "w") as fp:
            fp.write(markdown_content)
