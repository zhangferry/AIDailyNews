import unittest
import workflow.article.rss as rss
import workflow.mainflow as mainflow


class MyTestCase(unittest.TestCase):
    def test_parse_webpage(self):
        url = "https://holyswift.app/xcode-15-new-feature-streamlined-accessibility-audits/"
        content = rss.parse_web_page(url)
        print(content)

    def test_image_rss(self):
        configs = rss.load_rss_configs()
        image_config = None
        for config in configs:
            if config.get("type") == "image":
                image_config = config

        article = rss.parse_rss_item(image_config)
        res = mainflow.find_favorite_article(article)
        print(res)


if __name__ == '__main__':
    unittest.main()
