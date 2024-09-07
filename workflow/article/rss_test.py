import unittest, os
import workflow.article.rss as rss
from dateutil import tz
from datetime import datetime


class RssTestCase(unittest.TestCase):

    def setUp(self) -> None:
        os.environ["https_proxy"] = "http://127.0.0.1:465"
        os.environ["http_proxy"] = "http://127.0.0.1:465"
        os.environ["all_proxy"] = "http://127.0.0.1:465"

    def test_parse_cover_rss(self):
        config = {
            "title": "Changelogs Archive - The GitHub Blog",
            "url": "https://developer.apple.com/news/rss/news.rss",
            "image_enable": True    # 提取图片
        }
        articles = rss.parse_rss_config(config)
        for item in articles:
            print(item.link)

    def test_parse_rss(self):
        config = {
            "title": "The Register",
            "url": "https://rsshub.app/xiaoyuzhou/podcast/66d9e2a3bfd7110df48e4adf",
            "feature": "GitHub Trends Weekly"
        }
        articles = rss.parse_rss_config(config)
        for item in articles:
            print(f"link: {item.link}, summary: {item.summary}")

    def test_parse_code_rss(self):
        config = {
            "title": "Github",
            "url": "https://rsshub.app/github/trending/daily/swift",
            "type": "code"
        }
        articles = rss.parse_rss_config(config)
        for item in articles:
            print(item.link)

        assert len(articles) == 3

    def test_time_zone(self):
        cn_time_zone = "Asia/Shanghai"
        us_time_zone = "America/Detroit"
        unify_time_zone = tz.gettz(us_time_zone)

        date = datetime.today().astimezone(unify_time_zone)
        print(date)

    def target_config(self, type_name):
        configs = rss.load_rss_configs("./../resources")
        target_config = None
        for config in configs:
            if config.get("type") == type_name:
                target_config = config
            else:
                continue
        return target_config


class WebPageTestCase(unittest.TestCase):

    def test_parse_webpage(self):
        url = "https://www.theverge.com/2024/9/3/24234777/microsoft-apple-cloud-gaming-app-store-changes-xbox-cma"
        content = rss.parse_web_page(url)
        print(content)
        # h2 check

    def test_parse_github(self):
        # url = "https://t.co/wmWNbu8bVn"
        url = "https://github.com/hmlongco/Factory"
        content = rss.parse_github_readme(url)
        print(content)


if __name__ == '__main__':
    unittest.main()
