import unittest, os
from workflow.gpt.summary import evaluate_article_with_gpt, transform2json
from workflow.article.rss import Article, gen_article_from
from dotenv import load_dotenv


class SummaryTestCase(unittest.TestCase):

    def setUp(self):
        load_dotenv(dotenv_path="./../test_resources/.env")

    def test_gpt(self):
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

    def test_transform2json(self):
        input = """
        [{"link": "https://www.theverge.com/2024/9/3/24234777/microsoft-apple-cloud-gaming-app-store-changes-xbox-cma", "title": "微软和苹果再次争论云游戏应用", "tags": ["技术"], "score": 6, "summary": "微软和苹果再次就云游戏应用争论不休，微软希望 App Store 做出更多改变，而苹果则表示它有助于支持 iOS 上的云游戏应用。"}, {"link": "https://apps.apple.com/us/app/sleep-sounds-sunrise-alarm/id6502920973", "title": "睡眠声音和日出闹钟", "tags": ["应用"], "score": 8, "summary": "在全黑屏幕和放松的睡眠声音中入睡，然后在日出闹钟的自然光中轻轻醒来。这是同类中唯一一款应用！立即下载！"}, {"link": "https://github.com/freedmand/textra", "title": "textra", "tags": ["技术"], "score": 9, "summary": "textra 是一个命令行应用程序，它使用 Apple 的 Vision 和 Speech API 从图像、PDF 和音频文件中提取文本。它易于安装和使用，并提供各种输出选项，包括文本、页面文本和位置文本。textra 是从各种来源提取文本的强大工具。它对于研究人员、记者和任何需要从非文本文件获取文本的人来说都是一个有用的工具。它也是一个开源项目，这意味着它可以免费使用和修改。如果您正在寻找一种从图像、PDF 和音频文件中提取文本的简单而有效的方法，那么 textra 是一个不错的选择。它易于使用，功能强大，并且是开源的。"]}
        """
        output_list = transform2json(input)
        print(output_list)


if __name__ == '__main__':
    unittest.main()
