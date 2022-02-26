import requests
import bs4


class Reporter:
    def simple_crawl(self, url, tag, selector):
        r = requests.get(url)
        soup = bs4.BeautifulSoup(r.text, "html.parser")
        titlelinks = soup.findAll(tag, selector)
        headlines = list(map(lambda x: x.text, titlelinks))
        print(str(headlines))
        return str(headlines)[:1499]

    def fetch_hacker_news(self):
        return self.simple_crawl(
            url="https://news.ycombinator.com/newest",
            tag="a",
            selector={"class": "titlelink"},
        )

    def fetch_yonhapnews_news(self):
        return self.simple_crawl(
            url="https://www.yonhapnewstv.co.kr/news/headline",
            tag="a",
            selector={"class": "title"},
        )

    def fetch_cnbc_finance_news(self):
        return self.simple_crawl(
            url="https://www.cnbc.com/finance/",
            tag="a",
            selector={"class": "Card-title"},
        )

    def publish_letters(self):
        hacker_news = {"title": "hacker news", "content": self.fetch_hacker_news()}
        yonhapnews_news = {"title": "연합뉴스", "content": self.fetch_yonhapnews_news()}
        cnbc_finance_news = {
            "title": "cnbc finance news",
            "content": self.fetch_finance_news(),
        }
        return [hacker_news, yonhapnews_news, cnbc_finance_news]
