import os, json
from workflow.gpt.summary import request_gpt
import workflow.article.rss as rss_manager


def parse_daily_rss_article():
    """获取今日文章"""
    rss_items = rss_manager.load_rss_configs()

    daily_article = []
    for item in rss_items:
        rss_list = rss_manager.parse_rss_item(item)
        for rss in rss_list:
            daily_article.append(rss)
            print(f"date: {rss.date}, link: {rss.link}\ncontent: {rss.summary}")
    return find_favorite_article(daily_article)


def find_favorite_article(rss_articles):
    """获取评分最高的5篇"""
    final_list = []
    # 因gemini限流，文章最多分析20篇
    image_list = []
    rss_articles = rss_articles[:20]
    for article in rss_articles:
        # 图片格式内容不做评分
        if article.type == "image":
            image_list.append({"rss": article})
            continue
        if not article.summary:
            continue
        summary = evaluate_article(article.summary)
        if not summary:
            continue
        summary["rss"] = article
        final_list.append(summary)

    final_list.sort(key=lambda x: x["score"], reverse=True)

    # 仅输出评分最高的几篇文章
    max_nums = int(os.environ.get("MAX_ARTICLE_NUMS", "6"))
    result = final_list[:max_nums] + image_list[:1]
    return result


def evaluate_article(content):
    text = request_gpt(content)
    # 去掉首尾两行就是完整json内容
    text = text.removeprefix("```json")
    text = text.removesuffix("```")
    # 有时输出格式可能不完全符合json
    try:
        json_obj = json.loads(text)
        # 关键信息校验
        if json_obj.get("score"):
            return json_obj
        return None
    except:
        return None
