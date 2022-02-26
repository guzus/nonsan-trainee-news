import unittest
import sys

sys.path.append("src")
from config import EMAIL, PASSWORD
from reporter import Reporter
from spy import Spy
from postman import Postman


class ReporterTest(unittest.TestCase):
    def test_fetch_hacker_news(self):
        res = Reporter().fetch_hacker_news()
        self.assertIsNotNone(res)
        self.assertLess(len(res), 1500)

    def test_fetch_yonhapnews_news(self):
        res = Reporter().fetch_yonhapnews_news()
        self.assertIsNotNone(res)
        self.assertLess(len(res), 1500)

    def test_fetch_cnbc_finance_news(self):
        res = Reporter().fetch_cnbc_finance_news()
        self.assertIsNotNone(res)
        self.assertLess(len(res), 1500)


class SpyTest(unittest.TestCase):
    def test_get_soldiers_from_readme(self):
        res = Spy().get_soldiers_from_readme()
        self.assertIsNotNone(res)


class PostmanTest(unittest.TestCase):
    def test_send_letters(self):
        import thecampy

        res = Postman(email=EMAIL, password=PASSWORD).send_letters(
            letters=[{"title": "test", "content": "test!"}],
            soldiers=[
                thecampy.Soldier(
                    "구저스",
                    "20010301",
                    "20010401",
                    "육군훈련소",
                ).add_soldier_code("123")
            ],
        )
        self.assertIsNotNone(res)


if __name__ == "__main__":
    unittest.main()
