# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    user_name = scrapy.Field()#用户名
    followees = scrapy.Field()
    followers = scrapy.Field()
    introduce = scrapy.Field()
    ellipsis = scrapy.Field()
    head_image = scrapy.Field()
    main_page = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()



