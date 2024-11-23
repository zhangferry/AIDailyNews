import json

from dotenv import load_dotenv
from loguru import logger

from workflow.gpt.prompt import multi_content_prompt
from workflow.gpt.request import AIProvider


def evaluate_article_with_gpt(articles):
    load_dotenv()

    article_links = [article.link for article in articles]
    logger.info(f"start summary: {article_links}")

    gpt_input = ""
    for idx, item in enumerate(articles):
        gpt_input += f"```link: {item.link}, content:{item.summary}```.\n"

    ai_provider: AIProvider = AIProvider.build_from_envs()
    response = ai_provider.request(prompt=multi_content_prompt, content=gpt_input)
    response_list = transform2json(response)
    if not response_list:
        return []
    if not isinstance(response_list, list):
        # 有时单个内容未按数组格式输出
        response_list = [response_list]

    evaluate_list = [item for item in response_list if item.get("title") and item.get("link")]
    return evaluate_list


def transform2json(result):
    if not result:
        return None
    format_json = None
    # 去掉首尾两行就是完整json内容
    text = result.removeprefix("```json")
    text = text.removesuffix("```")
    # 有时输出格式可能不完全符合json
    try:
        json_obj = json.loads(text)
        # 关键信息校验
        format_json = json_obj
    except Exception as e:
        logger.exception(f"{e}")
    finally:
        return format_json
