# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeixinItem(scrapy.Item):
    title = scrapy.Field()
    desc = scrapy.Field()
    link = scrapy.Field()
    keyword = scrapy.Field()