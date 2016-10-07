# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonItem

class amazon(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['www.amazon.cn']
    start_urls = ['https://www.amazon.cn/s/ref=sr_pg_1?rh=i%3Aaps%2Ck%3Apython&page=1&keywords=python&ie=UTF8']

    def parse(self, response):
        allli = response.xpath('//li[@class = "s-result-item  celwidget "]')
        item = AmazonItem()
        for ali in allli:
            title = ali.xpath('div/div[3]/div[1]/a/@title').extract()
            link = ali.xpath('div/div[3]/div[1]/a/@href').extract()
            book_type = ali.xpath('div/div[4]/a/h3/@data-attribute').extract()
            price = ali.xpath('div/div[5]/a/span/text()').extract()
            if title:
                item['title'] = title[0]
            else:
                print('没有信息')
            if link:
                item['link'] = link[0]
            if book_type:
                item['book_type'] = book_type[0]
            if price:
                item['price'] = price[0]
            yield item
        urlss = response.xpath('//*[@id="pagn"]/span[@class = "pagnDisabled"]/text()').extract()
        if urlss:
            urls = int(urlss[0])
            for i in range(2,urls+1):
                url = 'https://www.amazon.cn/s/ref=sr_pg_%d'%i+'?rh=i%3Aaps%2Ck%3Apython&page='+'%d&keywords=python&ie=UTF8'%i
                yield scrapy.Request(url,callback=self.parse)
