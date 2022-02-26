import requests
import bs4


class Reporter:
    def fetch_hacker_news(self):
        r = requests.get("https://news.ycombinator.com/newest")
        soup = bs4.BeautifulSoup(r.text, "html.parser")
        titlelinks = soup.findAll("a", {"class": "titlelink"})
        headlines = list(map(lambda x: x.text, titlelinks))
        print(str(headlines))
        return str(headlines)[:1499]

    def fetch_yonhapnews_news(self):
        r = requests.get("https://www.yonhapnewstv.co.kr/news/headline")
        soup = bs4.BeautifulSoup(r.text, "html.parser")
        titlelinks = soup.findAll("a", {"class": "title"})
        headlines = list(map(lambda x: x.text, titlelinks))
        print(str(headlines))
        return str(headlines)[:1499]

    def fetch_finance_news(self):
        return ""

    def publish_letters(self):
        hacker_news = {"title": "hacker news", "content": self.fetch_hacker_news()}
        yonhapnews_news = {"title": "연합뉴스", "content": self.fetch_yonhapnews_news()}
        return [hacker_news, yonhapnews_news]
