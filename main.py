import workflow.mainflow as mainflow
from dotenv import load_dotenv
from loguru import logger
import os

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    load_dotenv()
    logger.info(f"envs: {os.environ}")

    # os.environ["https_proxy"] = "http://127.0.0.1:465"
    # os.environ["http_proxy"] = "http://127.0.0.1:465"
    # os.environ["all_proxy"] = "http://127.0.0.1:465"

    mainflow.execute()
