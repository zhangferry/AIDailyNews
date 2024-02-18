import datetime, os


class Blog:
    metadata: str
    guide: str
    news: str
    code: str

    def __init__(self, metadata, guide, news, code):
        self.metadata = metadata
        self.guide = guide
        self.news = news
        self.code = code

    def make_blog(self):
        return self.metadata + self.guide + self.news + self.code


def make_daily_markdown_with(articles):
    news_articles = []
    code_articles = []
    tags = []
    article_titles = []

    for article in articles:
        if article.type == "code":
            code_articles.append(article)
        else:
            news_articles.append(article)

        tags.extend(article.evaluate.get("tags", []))
        article_titles.append(article.evaluate["title"])

    md_path, meta_data = make_meta_data(description="\n".join(article_titles), tags=tags)
    daily_guide = make_daily_guide(article_titles)
    daily_news = make_daily_news(news_articles)
    daily_code = make_daily_code(code_articles)

    blog = Blog(metadata=meta_data, guide=daily_guide, news=daily_news, code=daily_code)
    print(f"make blog success: {meta_data}")
    with open(md_path, "w") as fp:
        fp.write(blog.make_blog())
        print(f"write to file: {md_path}")


def make_meta_data(description, tags):
    today_str = datetime.date.today().strftime("%Y-%m-%d")

    current_directory = os.path.dirname(os.path.abspath(__file__))
    # 获取当前项目的根目录
    project_root = os.path.dirname(current_directory)
    blog_folder = f"{project_root}/../src/content/blog"

    md_title = f"iOS Daily News #{today_str}"

    tags_str = "".join([f"- '{tag}'\n" for tag in set(tags)])

    data = f"""---
title: "{md_title}"
date: "{datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")}"
author: 摸鱼仔
description: "{description}"
tags: 
{tags_str}
---
"""

    path = f"{blog_folder}/iOSDailyNews_{today_str}.md"

    return path, data


def make_daily_news(articles):
    if not articles:
        return ""
    news_content = "## Daily News"
    for article in articles:
        article_intro = f"""
### [{article.evaluate["title"]}]({article.link})

来源：{article.info["title"]}

发布时间：{article.date}

{article.evaluate["summary"]}
"""
        news_content += article_intro
    return news_content


def make_daily_code(articles):
    if not articles:
        return ""
    news_content = "## Daily Code"
    for article in articles:
        article_intro = f"""
### [{article.evaluate["title"]}]({article.link})
 
{article.evaluate["summary"]}
"""
        news_content += article_intro
    return news_content


def make_daily_guide(titles):
    guide = "".join([f"> * {item}\n" for item in titles])
    return f"\n{guide}\n"
