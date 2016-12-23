# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    subject = scrapy.Field()
    contents = scrapy.Field()
    language = scrapy.Field()
    keyword_1 = scrapy.Field()
    keyword_2 = scrapy.Field()
