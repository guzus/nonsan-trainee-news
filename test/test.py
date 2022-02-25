import unittest
import sys

sys.path.append("../src")
from reporter import Reporter


class ReporterTest(unittest.TestCase):
    def test_fetch_hacker_news(self):
        res = Reporter().fetch_hacker_news()
        self.assertIsNotNone(res)

    def test_fetch_yonhapnews_news(self):
        res = Reporter().fetch_yonhapnews_news()
        self.assertIsNotNone(res)


if __name__ == "__main__":
    unittest.main()
