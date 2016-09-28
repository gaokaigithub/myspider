# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.exceptions import DropItem
from .items import WeixinItem

class WeixinPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient('localhost',27017)
        self.db = connection['weixin']
        self.coll = self.db['weixin']
    def process_item(self,item,spider):
        if isinstance(item,WeixinItem):
            self.save_or_update(self.coll,item)

    def save_or_update(self,collection,item):
        try:
            collection.insert(dict(item))
            return item
        except:
            raise DropItem('此处有重复')





