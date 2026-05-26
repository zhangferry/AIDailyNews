import json
import re

from dotenv import load_dotenv
from loguru import logger

from workflow.gpt.prompt import multi_content_prompt
from workflow.gpt.request import AIProvider


def evaluate_article_with_gpt(articles):
    load_dotenv()

    article_links = [article.link for article in articles]
    logger.info(f"start summary: {article_links}")

    gpt_input = json.dumps(
        [
            {
                "title": item.title,
                "link": item.link,
                "source": item.info.get("title", "") if item.info else "",
                "category": item.config.get("category", "") if item.config else "",
                "date": item.date,
                "content": item.summary,
            }
            for item in articles
        ],
        ensure_ascii=False,
    )

    ai_provider: AIProvider = AIProvider.build_from_envs()
    response = ai_provider.request(prompt=multi_content_prompt, content=gpt_input)
    response_list = transform2json(response)
    if not response_list:
        return []
    if not isinstance(response_list, list):
        # 有时单个内容未按数组格式输出
        response_list = [response_list]

    evaluate_list = [item for item in response_list if item.get("title") and item.get("link")]
    # Normalize summary formatting: ensure section headers are bold and separated by double line breaks
    for item in evaluate_list:
        if item.get("summary"):
            item["summary"] = normalize_summary(item["summary"])
    return evaluate_list


def normalize_summary(summary: str) -> str:
    """Ensure summary sections use bold headers and consistent double line breaks."""
    import re
    # Ensure section markers are bold (wrapped in **)
    summary = re.sub(
        r'(?<!\*)\*?(背景[/／]问题|核心观点[/／]方案|结论[/／]价值)\*?(?!\*)',
        r'**\1**',
        summary,
    )
    # Normalize line breaks before section headers: consume any existing \n, then use exactly \n\n
    summary = re.sub(
        r'\n*(\*\*(?:背景[/／]问题|核心观点[/／]方案|结论[/／]价值)\*\*)',
        r'\n\n\1',
        summary,
    )
    return summary.strip()


def transform2json(result):
    if not result:
        return None
    format_json = None
    text = result.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)

    json_match = re.search(r"(\[[\s\S]*\]|\{[\s\S]*\})", text)
    if json_match:
        text = json_match.group(1)

    try:
        json_obj = json.loads(text)
        # 关键信息校验
        format_json = json_obj
    except Exception as e:
        logger.exception(f"{e}")
    finally:
        return format_json
