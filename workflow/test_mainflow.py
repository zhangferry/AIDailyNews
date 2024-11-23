import unittest, os
import workflow.mainflow as flow


class MyTestCase(unittest.TestCase):

    def setUp(self):
        # os.environ["https_proxy"] = "http://127.0.0.1:465"
        # os.environ["http_proxy"] = "http://127.0.0.1:465"
        # os.environ["all_proxy"] = "http://127.0.0.1:465"
        pass

    def test_mainflow_flow(self):
        """
        test_resources is same peer with resources for test, you should add .env and rss.json
        """
        rss_resource_path = "test_resources"
        flow.execute(rss_resource_path)


if __name__ == '__main__':
    unittest.main()
