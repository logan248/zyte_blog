import scrapy
from ..items import ZyteBlogItem


class ZyteSpider(scrapy.Spider):
    name = 'zyte'

    page_number = 2

    #allowed_domains = ['zyte.com']

    start_urls = ['https://www.zyte.com/blog/']

    def parse(self, response):

        items = ZyteBlogItem()

        date = [d.strip() for d in response.css(
            '.oxy-post-image-date-overlay::text').extract()]
        article = response.css('.oxy-post-title::text').extract()
        author = [a.strip() for a in response.css(
            '.oxy-post-meta-author::text').extract()]
        author = [a for a in author if a.startswith('By')]
        reading_time = [f'{r.strip()} Mins' for r in response.css(
            '.rt-time::text').extract()]

        links = [f'https://www.zyte.com{link}' for link in response.css(
            '.oxy-read-more::attr(href)').extract()]

        items['date'] = date
        items['article'] = article
        items['author'] = author
        items['reading_time'] = reading_time
        items['link_to_article'] = links

        yield items

        #next_page = f'https://www.zyte.com/blog/page/{ZyteSpider.page_number}/'

        #if ZyteSpider.page_number <= 20:
        #    yield response.follow(next_page, callback=self.parse)
        #    ZyteSpider.page_number += 1
