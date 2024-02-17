import unittest, os
import workflow.article.rss as rss
import workflow.mainflow as mainflow


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        os.environ["https_proxy"] = "http://127.0.0.1:465"
        os.environ["http_proxy"] = "http://127.0.0.1:465"
        os.environ["all_proxy"] = "http://127.0.0.1:465"

    def test_parse_webpage(self):
        url = "https://holyswift.app/xcode-15-new-feature-streamlined-accessibility-audits/"
        content = rss.parse_web_page(url)
        print(content)

    def test_parse_github(self):
        url = "https://github.com/hmlongco/Factory"
        content = rss.parse_github_readme(url)
        print(content)

    def test_parse_image_rss(self):
        article = rss.parse_rss_item(self.target_config("image"))
        res = mainflow.find_favorite_article(article)
        print(res)

    def test_parse_link_rss(self):
        articles = rss.parse_rss_item(self.target_config("link"))
        print(articles)
        res = mainflow.find_favorite_article(articles)
        print(res)

    def test_parse_code_rss(self):
        articles = rss.parse_rss_item(self.target_config("code"))
        print(articles)
        res = mainflow.find_favorite_article(articles)
        print(res)

    def target_config(self, type_name):
        configs = rss.load_rss_configs("./../resources")
        target_config = None
        for config in configs:
            if config.get("type") == type_name:
                target_config = config
        return target_config


if __name__ == '__main__':
    unittest.main()
