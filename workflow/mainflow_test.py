import unittest, os
import workflow.mainflow as flow
from dotenv import load_dotenv


class MyTestCase(unittest.TestCase):

    def setUp(self):
        os.environ["https_proxy"] = "http://127.0.0.1:465"
        os.environ["http_proxy"] = "http://127.0.0.1:465"
        os.environ["all_proxy"] = "http://127.0.0.1:465"

        load_dotenv()

    def test_flow(self):

        rss_resource_path = "resources/code.json"
        flow.execute(rss_resource_path)


if __name__ == '__main__':
    unittest.main()
