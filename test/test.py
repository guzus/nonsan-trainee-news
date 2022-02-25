import unittest
import sys

sys.path.append("../src")
from reporter import Reporter
from spy import Spy


class ReporterTest(unittest.TestCase):
    def test_fetch_hacker_news(self):
        res = Reporter().fetch_hacker_news()
        self.assertIsNotNone(res)

    def test_fetch_yonhapnews_news(self):
        res = Reporter().fetch_yonhapnews_news()
        self.assertIsNotNone(res)

class SpyTest(unittest.TestCase):
    def test_get_soldiers_from_readme(self):
        res = Spy().get_soldiers_from_readme()
        self.assertIsNotNone(res)

if __name__ == "__main__":
    unittest.main()
