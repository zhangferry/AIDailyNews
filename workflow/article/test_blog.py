import unittest
from workflow.article.rss import Article
from workflow.article.blog import make_daily_markdown_with


class MyTestCase(unittest.TestCase):

    def test_blog(self):
        evaluate = {
            "score": 99,
            "tags": ["Apple Cash", "Apple Card"],
            "title": "🍎苹果公司为Apple Cash用户推出了新的Apple Card 虛擬卡功能",
            "summary": "苹果公司正在调查影响部分 Apple Watch Series 9 和 Apple Watch Ultra 2 显示屏的触摸相关问题。该问题可能导致屏幕出现“跳动”或其他意外行为，甚至可能导致 Apple Watch 无意中拨打电话或无法输入设备密码。苹果建议用户保持 Apple Watch 软件的最新状态，并提供了强制重启设备的步骤。目前尚不清楚该问题有多普遍，也没有提供潜在修复的时间表。",
        }

        rss = Article(title="Apple Investigating 'Ghost Touches' Issue Affecting Some Series 9 and Ultra 2 Watches",
                      link="https://www.macrumors.com/2024/02/10/apple-watch-series-9-ultra-2-touch-screen-issue/",
                      date="2024-02-11 02:54:42",
                      category="Daily News",
                      summary="苹果公司正在调查影响部分 Apple Watch Series 9 和 Apple Watch Ultra 2 显示屏的触摸相关问题。该问题可能导致屏幕出现“跳动”或其他意外行为，甚至可能导致 Apple Watch 无意中拨打电话或无法输入设备密码。苹果建议用户保持 Apple Watch 软件的最新状态，并提供了强制重启设备的步骤。目前尚不清楚该问题有多普遍，也没有提供潜在修复的时间表。",
                      info={"title": "MacRumors"},
                      type_name="default",
                      evaluate=evaluate)

        make_daily_markdown_with([rss])


if __name__ == '__main__':
    unittest.main()
