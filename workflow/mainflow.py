from gpt.summary import request_gpt
import workflow.rss_manager as rss_manager
import json


def parse_daily_rss_article():
    """获取今日文章"""
    rss_items = rss_manager.load_rss_configs()

    daily_article = []
    for item in rss_items:
        rss = rss_manager.parse_rss_item(item)
        if rss:
            daily_article.append(rss)
            print(f"date: {rss.date}, link: {rss.link}")
    # daily_article = daily_article[:1]
    return find_favorite_article(daily_article)


def find_favorite_article(rss_articles):
    """获取评分最高的5篇"""
    final_list = []
    # 因gemini限流，文章最多分析20篇
    rss_articles = rss_articles[:20]
    for article in rss_articles:
        summary = evaluate_article(article.summary)
        summary["rss"] = article
        final_list.append(summary)

    final_list.sort(key=lambda x: x["score"], reverse=True)

    # 仅输出最高的5篇文章
    final_list = final_list[:5]
    return final_list


def evaluate_article(content):
    text = request_gpt(content)
    # 去掉首尾两行就是完整json内容
    text = text.removeprefix("```json")
    text = text.removesuffix("```")
    json_obj = json.loads(text)
    return json_obj
