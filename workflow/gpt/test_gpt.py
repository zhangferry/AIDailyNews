import unittest, os
from workflow.gpt.summary import evaluate_article_with_gpt
from workflow.article.rss import Article


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # optional, for proxy
        os.environ["https_proxy"] = "http://127.0.0.1:465"
        os.environ["http_proxy"] = "http://127.0.0.1:465"
        os.environ["all_proxy"] = "http://127.0.0.1:465"

        article1 = Article(link="https://techcrunch.com/2024/02/27/threads-widens-the-gap-with-x-with-triple-the-daily-downloads-on-ios/",
                          summary="29 February is causing problems in software systems across the globe. It’s a good reminder on how few assumptions we should make about dates – and why to use a date library when you can.")

        article2 = Article(link="https://swift.org",
                           summary="The Swift evolution process aims to leverage the collective ideas, insights, and experience of the Swift community to improve the Swift development experience. ")

        res = evaluate_article_with_gpt([article1, article2])
        # 4条结果
        assert len(res) == 2
        # 评分最高的内容包含Swift字符串
        item = res[-1]
        assert "Swift" in item["title"]


if __name__ == '__main__':
    unittest.main()
