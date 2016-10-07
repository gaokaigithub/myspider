# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class AmazonPipeline(object):

    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root',\
                                    password = 'gaokai1028',db = 'amazon',charset='utf8')
        self.cur = self.conn.cursor()
        self.cur.execute('create table if not exists book3(title varchar(255),link varchar(255),book_type varchar(255),price varchar(255))')

    def process_item(self, item, spider):
        if item.get('title'):
            self.cur.execute('insert into book3 values(%s,%s,%s,%s)',(item['title'],item['link'],\
                                                                         item['book_type'],item['price']))
            self.conn.commit()





