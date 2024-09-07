import unittest, os
from workflow.gpt.summary import evaluate_article_with_gpt, transform2json
from workflow.article.rss import Article


class SummaryTestCase(unittest.TestCase):
    def test_gpt(self):
        # optional, for proxy
        os.environ["https_proxy"] = "http://127.0.0.1:465"
        os.environ["http_proxy"] = "http://127.0.0.1:465"
        os.environ["all_proxy"] = "http://127.0.0.1:465"

        article1 = Article(link="https://www.theverge.com/2024/9/3/24234777/microsoft-apple-cloud-gaming-app-store-changes-xbox-cma",
                          summary="""Earlier this year Apple started opening up its App Store to game streaming services like Xbox Cloud Gaming and GeForce Now, freeing them from being restricted to web apps on the iPhone and iPad. Despite multiple changes to Apple’s App Store guidelines this year, Microsoft and Nvidia have still not published native cloud gaming apps for iOS, and Microsoft is now detailing exactly why.

Microsoft already said earlier this year that Apple’s cloud changes don’t go “far enough” for Xbox, but in submissions to the UK’s Competition and Markets Authority (CMA), Microsoft now argues that Apple’s changes in January, March, and April to its App Store guidelines (section 4.9 and 4.7) aren’t enough for it to operate a native Xbox Cloud Gaming app on iOS at all.

“Microsoft identified a number of other provisions in Apple’s Guidelines that continue to limit its ability to distribute and operate a Cloud Gaming iOS native app (namely Guidelines 2.1, 2.5.2, 2.5.6, 3.1.1, 3.1.2(a), 3.1.3(b), 3.2.2(i), 3.2.2(ii), 4.2.2., 4.2.7(e)),” said Microsoft in a filing to the CMA in late July.

Microsoft claims that Apple’s guidelines “still represent an obstacle to Cloud Gaming native apps” because it apparently can’t comply with them, both technically and economically, if it incorporates third-party games into its Xbox Cloud Gaming service on iOS. Microsoft specifically calls out Apple’s requirement for multiplatform services, like Xbox Cloud Gaming, to make all content, subscriptions, and features available within an iOS app as an in-app purchase (IAP):

In fact, Apple’s IAP commission fee is set at a level that is neither economically sustainable nor justifiable. The 30 percent commission fee makes it impossible for Microsoft to effectively monetize its cloud gaming service offering, given that Guideline 3.1.3(b) prevents different content, subscriptions or features (including consumables in multiplatform games) being offered to iOS users (as compared to the content, subscriptions and features offered on other platforms).

As observed by the CMA in its Mobile Ecosystem market study, the 30 percent fee imposed by Apple on IAPs is the result of a lack of competition in the distribution of native iOS apps.


Microsoft also claims third-party game developers would need to recode their games to comply with the IAP requirement.

Microsoft also takes issue with Apple’s 3.1.1 guideline, which prevents iOS app developers from linking outside to enable the purchase of subscriptions. Apple provides an exception for “Reader” apps, but cloud gaming apps don’t qualify for this exception. Apple argues in its filing with the CMA that it has “never approved a gaming app to take advantage of the Reader Rule,” so it says app developers shouldn’t be calling into question its approach to in-app purchases in the context of cloud gaming.

The CMA is currently carrying out a market investigation into mobile browsers, browser engines, and the distribution of cloud gaming services through app stores in the UK. It has identified a number of possible remedies to address competition concerns around cloud gaming apps on mobile devices, including potentially requiring Apple to enable cloud gaming native apps to operate on a “read-only” basis with no in-game purchases or subscriptions so that games don’t need to be re-coded.

The CMA is also considering requiring Apple and Google to allow cloud gaming service providers to incorporate their own in-app payment systems, and potential requirements for Apple to amend its guidelines to remove elements that may contain technical restrictions on cloud gaming apps.

Apple argues that it supports cloud gaming via web apps, and even cites two Verge articles that cover Microsoft’s improvements to Xbox Cloud Gaming performance on iPhone and iPad and that more than 20 million people have used Xbox Cloud Gaming. “It is notable that while CMA cites Microsoft’s concerns in the Working Paper, Microsoft has chosen not to engage with Apple on cloud gaming apps since Apple’s changes to the Guideline,” says Apple. “This lack of engagement comes despite Apple’s affirmative outreach on new opportunities and tools for cloud gaming apps on iOS.”

Apple also argues that developers “...generally are not having difficulty with the IPA requirement” and then cites Antstream, a small app developer that launched the first iPhone game streaming service in the App Store earlier this year with more than 1,300 retro titles from Atari, Amiga, and Nintendo consoles. Apple helped Antstream with subscription optimizations, editorial frameworks, and even public relations review and guidance for its launch announcement.

The CMA has set a deadline for all parties to respond to its market investigation for this month before it plans to publish a provisional decision report in November. There will then be plenty of time for Microsoft and Apple to continue arguing between November and December, ahead of a final report in either February or March next year.""")

        article2 = Article(link="https://swift.org",
                           summary="The Swift evolution process aims to leverage the collective ideas, insights, and experience of the Swift community to improve the Swift development experience. ")

        res = evaluate_article_with_gpt([article1, article2])
        # 4条结果
        assert len(res) == 2
        # 评分最高的内容包含Swift字符串
        item = res[-1]
        assert "Swift" in item["title"]

    def test_transform2json(self):
        input = """
        [{"link": "https://www.theverge.com/2024/9/3/24234777/microsoft-apple-cloud-gaming-app-store-changes-xbox-cma", "title": "微软和苹果再次争论云游戏应用", "tags": ["技术"], "score": 6, "summary": "微软和苹果再次就云游戏应用争论不休，微软希望 App Store 做出更多改变，而苹果则表示它有助于支持 iOS 上的云游戏应用。"}, {"link": "https://apps.apple.com/us/app/sleep-sounds-sunrise-alarm/id6502920973", "title": "睡眠声音和日出闹钟", "tags": ["应用"], "score": 8, "summary": "在全黑屏幕和放松的睡眠声音中入睡，然后在日出闹钟的自然光中轻轻醒来。这是同类中唯一一款应用！立即下载！"}, {"link": "https://github.com/freedmand/textra", "title": "textra", "tags": ["技术"], "score": 9, "summary": "textra 是一个命令行应用程序，它使用 Apple 的 Vision 和 Speech API 从图像、PDF 和音频文件中提取文本。它易于安装和使用，并提供各种输出选项，包括文本、页面文本和位置文本。textra 是从各种来源提取文本的强大工具。它对于研究人员、记者和任何需要从非文本文件获取文本的人来说都是一个有用的工具。它也是一个开源项目，这意味着它可以免费使用和修改。如果您正在寻找一种从图像、PDF 和音频文件中提取文本的简单而有效的方法，那么 textra 是一个不错的选择。它易于使用，功能强大，并且是开源的。"]}
        """
        output_list = transform2json(input)
        print(output_list)


if __name__ == '__main__':
    unittest.main()
