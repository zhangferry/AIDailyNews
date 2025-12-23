import unittest, os

from workflow.gpt.summary import evaluate_article_with_gpt, AIProvider
from workflow.article.rss import gen_article_from
from workflow.gpt.prompt import multi_content_prompt
from workflow.gpt.request import request_openai
from dotenv import load_dotenv
import workflow.article.rss as rss


class SummaryTestCase(unittest.TestCase):

    def setUp(self):
        """
        test_resources is same peer with resources for test
        """
        # load_dotenv(dotenv_path="./../test_resources/.env")
        ip = "127.0.0.1:7897"
        os.environ["https_proxy"] = f"http://{ip}"
        os.environ["http_proxy"] = f"http://{ip}"
        # os.environ["all_proxy"] = f"socks5://{ip}"
        load_dotenv()

    def test_gpt_request(self):
        # provider = AIProvider.build_from_envs()

        config = {
            "title": "Github",
            "url": "https://rsshub.zhangferry.com/github/trending/weekly/swift",
            "type": "code"
        }
        articles = rss.parse_rss_config(config)
        evaluate_list = evaluate_article_with_gpt(articles)
        print(evaluate_list)

    def test_evaluate_article_with_gpt(self):
        # optional, for proxy
        # os.environ["https_proxy"] = "http://127.0.0.1:465"
        # os.environ["http_proxy"] = "http://127.0.0.1:465"
        # os.environ["all_proxy"] = "http://127.0.0.1:465"

        rss_item = {
            "link": "https://github.com/groue/GRDB.swift",
            "title": "grdb.swift"
        }

        article = gen_article_from(rss_item=rss_item, rss_type="code")
        res = evaluate_article_with_gpt([article])
        print(res)


if __name__ == '__main__':
    unittest.main()
