import scrapy
from ..settings import *
from ..items import WeixinItem

class weixin(scrapy.Spider):
    name = 'weixin'
    allowed_urls = ['www.sogou.com']

    def start_requests(self):
        for i in range(1,int(PAGES)+1):
            wurls = "http://weixin.sogou.com/weixin?query=%s&type=2&page=%d&ie=utf8"%(KEYWORD,i)
            yield self.make_requests_from_url(wurls)
    def make_requests_from_url(self, url):
        return scrapy.Request(url,headers=WEIXIN_HEADER,cookies=WEIXIN_COOKIE)
    def parse(self, response):
        item = WeixinItem()
        titles = response.xpath('//div[@class="wx-rb wx-rb3"]/div[2]/h4/a/text()').extract()
        urls = response.xpath('//div[@class="wx-rb wx-rb3"]/div[2]/h4/a/@href').extract()
        descs = response.xpath('//div[@class="wx-rb wx-rb3"]/div[2]/p/text()').extract()
        print(response.headers.getlist('Set-Cookie'))
        for title in titles:
            item['title'] = title
        for url in urls:
            item['link'] = url
            print(url)
        yield item








