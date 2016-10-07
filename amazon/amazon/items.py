# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    book_type = scrapy.Field()
    link = scrapy.Field()