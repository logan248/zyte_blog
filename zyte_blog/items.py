# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZyteBlogItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()
    article = scrapy.Field()
    author = scrapy.Field()
    reading_time = scrapy.Field()
    link_to_article = scrapy.Field()
