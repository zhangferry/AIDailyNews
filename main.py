import workflow.mainflow as mainflow
from dotenv import load_dotenv
from loguru import logger
import os

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    load_dotenv()
    # 只记录非敏感的环境变量
    safe_envs = {k: v for k, v in os.environ.items()
                 if not any(sensitive in k.upper()
                           for sensitive in ['KEY', 'TOKEN', 'SECRET', 'PASSWORD', 'AUTH'])}
    logger.info(f"环境配置已加载: {safe_envs}")

    # os.environ["https_proxy"] = "http://127.0.0.1:465"
    # os.environ["http_proxy"] = "http://127.0.0.1:465"
    # os.environ["all_proxy"] = "http://127.0.0.1:465"

    mainflow.execute()
