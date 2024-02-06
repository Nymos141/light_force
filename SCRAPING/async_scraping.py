# import httpx
# import asyncio
# from parsel import Selector
#
# class AsyncScraper:
#     NEWS_URL = "https://www.france24.com/en/"
#     HEADERS = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
#         "Accept": "*/*",
#         "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
#         "Accept-Encoding": "gzip, deflate, br"
#     }
#
#     LINK_XPATH = '//div[@class="article__title "]/a/@href'
#     IMG_XPATH = '//figure[@class="m-figure m-figure--16x9"]//img/@src'
#
#     async def fetch(self, url):
#         async with httpx.AsyncClient() as client:
#             response = await client.get(url, headers=self.HEADERS)
#             return response.text
#
#     async def parse(self, url):
#         html = await self.fetch(url)
#         tree = Selector(text=html)
#
#         links = tree.xpath(self.LINK_XPATH).getall()
#         img_urls = tree.xpath(self.IMG_XPATH).getall()
#
#         news_data = []
#
#         for i, link in enumerate(links):
#             news_entry = {
#                 'link': self.NEWS_URL + link,
#                 'img_url': img_urls[i] if i < len(img_urls) else None
#             }
#             news_data.append(news_entry)
#
#         return news_data
#
#     async def scrape(self):
#         return await self.parse(self.NEWS_URL)
#
#
# if __name__ == "__main__":
#     scraper = AsyncScraper()
#     asyncio.run(scraper.scrape())
