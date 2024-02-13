import datetime, os


def make_markdown_with(articles):
    today_str = datetime.date.today().strftime("%Y-%m-%d")
    tags = []   # 表示分类

    current_directory = os.path.dirname(os.path.abspath(__file__))
    # 获取当前项目的根目录
    project_root = os.path.dirname(current_directory)
    blog_folder = f"{project_root}/../src/content/blog"

    count = 0
    for file in os.listdir(blog_folder):
        if file.endswith(".md"):
            count += 1

    md_title = f"iOS Daily News #{count + 1} ({today_str})"
    md_path = f"{blog_folder}/iOSDailyNews_{today_str}.md"

    markdown_content = ""
    image_info = None
    article_titles = []

    for article in articles:
        rss = article["rss"]
        if rss.type == "image":
            image_info = rss
            continue

        source = rss.info["title"]
        tags.extend(article.get("tags", []))
        article_titles.append(article["title"])

        article_intro = f"""
## [{article["title"]}]({rss.link})

来源：{source}

发布时间：{rss.date}

{article["summary"]}
        """
        markdown_content += article_intro

    tags = "".join([f"- '{tag}'\n" for tag in set(tags)])
    description = "\n".join(article_titles)
    header = f"""---
title: "{md_title}"
date: "{datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")}"
author: 摸鱼仔
description: "{description}"
tags: 
{tags}
---
    """

    image_content = f"""
## Daily wallpaper

![{image_info.title}]({image_info.summary})

来源：{image_info.link}
    """ if image_info else ""

    with open(md_path, "w") as fp:
        fp.write(header + image_content + markdown_content)
