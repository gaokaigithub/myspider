import scrapy
from ..items import ZhihuItem
from ..settings import *

class zhihu_spider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/people/chi-chu-63']

    def start_requests(self):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def make_requests_from_url(self, url):
        return scrapy.Request(url,headers=ZHIHU_HEADER,cookies=ZHIHU_COOKIE)

    def parse(self, response):
        item = ZhihuItem()
        user_name = response.xpath('/html/body/div[3]/div[1]/div/div[1]/div[1]/div/div[1]/div[2]/span/text()')[0].extract()
        print(user_name)
        if user_name:
            item['user_name'] = user_name
        follow = response.xpath('/html/body/div[3]/div[2]/div[1]/a/strong/text()').extract()
        if follow:
            item['followees'] = int(follow[0])
            item['followers'] = int(follow[1])

        item['introduce'] = ''.join(response.xpath('/html/body/div[3]/div[1]/div/div[1]/div[1]/div/div[2]/div/div[2]/span[1]/span[2]/span/text()')[0].extract())
        item['ellipsis'] = ''.join(response.xpath('/html/body/div[3]/div[1]/div/div[1]/div[1]/div/div[1]/div[2]/div/@title')[0].extract())
        head_url = response.xpath('/html/body/div[3]/div[1]/div/div[1]/div[1]/div/img/@src')[0].extract()
        arr = []
        arr.append(head_url)
        item['head_image'] = head_url
        item['image_urls'] = arr
        if response.url:
            item['main_page'] = response.url
        print(response.url)
        yield item
        url = 'https://www.zhihu.com' + response.xpath('/html/body/div[3]/div[2]/div[1]/a[1]/@href')[0].extract()
        yield scrapy.Request(url, callback=self.parse_followee, headers=ZHIHU_HEADER, cookies=ZHIHU_COOKIE)

    def parse_followee(self,response):
        follow_urls = response.xpath('//*[@id="zh-profile-follows-list"]/div/div/div[2]/h2/span/a/@href').extract()
        for url in follow_urls:
            yield scrapy.Request(url,callback=self.parse,headers=ZHIHU_HEADER,cookies=ZHIHU_COOKIE)










