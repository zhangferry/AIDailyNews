import unittest, os
from workflow.gpt.summary import request_gpt


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # optional, for proxy
        os.environ["https_proxy"] = "http://127.0.0.1:465"
        os.environ["http_proxy"] = "http://127.0.0.1:465"
        os.environ["all_proxy"] = "http://127.0.0.1:465"

        example_input = [
            """Several of Apple's display suppliers have proposed their prices for supplying
OLED displays for the fourth-generation iPhone SE,Apple Negotiating With OLED Suppliers for Next Year's iPhone SE",
            """,
            "short content",
            """29 February is causing problems in software systems across the globe. 
It’s a good reminder on how few assumptions we should make about dates – and why to use a date library when you can.
            """,
            """The Swift evolution process aims to leverage the collective ideas, insights, 
and experience of the Swift community to improve the Swift development experience. 
Its two primary goals are:
Engage the wider Swift community in the ongoing evolution of Swift, and
Maintain the vision and conceptual coherence of Swift.
There is a natural tension between these two goals. Open evolution processes are, by nature, chaotic. 
Yet, maintaining a coherent vision for something as complicated as a programming language requires some level of coordination. 
The Swift evolution process aims to strike a balance that best serves the Swift community as a whole.
            """
        ]

        res = request_gpt(example_input)
        # 4条结果
        assert len(res) == 4
        # 评分最高的内容包含Swift字符串
        item = res[-1]
        assert "Swift" in item["title"]


if __name__ == '__main__':
    unittest.main()
