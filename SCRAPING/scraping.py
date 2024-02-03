import requests
from parsel import Selector

class Scraper:
    NEWS_URL = "https://www.france24.com/en/"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
        "Accept": "*/*",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br"
    }

    LINK_XPATH = '//div[@class="article__title "]/a/@href'
    IMG_XPATH = '//figure[@class="m-figure m-figure--16x9"]//img/@src'

    def parse(self):
        text = requests.get(url=self.NEWS_URL, headers=self.HEADERS).text

        tree = Selector(text=text)
        links = tree.xpath(self.LINK_XPATH).getall()
        img_urls = tree.xpath(self.IMG_XPATH).getall()

        news_data = []

        for i, link in enumerate(links):
            news_entry = {
                'link': self.NEWS_URL + link,
                'img_url': img_urls[i] if i < len(img_urls) else None
            }
            news_data.append(news_entry)

        return news_data