import unittest, os

from  summary import evaluate_article_with_gpt, AIProvider
from workflow.article.rss import gen_article_from
from prompt import multi_content_prompt
from request import request_openai
from dotenv import load_dotenv


class SummaryTestCase(unittest.TestCase):

    def setUp(self):
        """
        test_resources is same peer with resources for test
        """
        load_dotenv(dotenv_path="./../test_resources/.env")

    def test_gpt_request(self):
        provider = AIProvider.build_from_envs()
        res = request_openai(provider=provider, prompt=multi_content_prompt, content="")
        print(res)

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
