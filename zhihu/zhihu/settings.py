# -*- coding: utf-8 -*-

# Scrapy settings for zhihu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihu'

SPIDER_MODULES = ['zhihu.spiders']
NEWSPIDER_MODULE = 'zhihu.spiders'
ZHIHU_COOKIE = {
"d_c0":"AEDA9KNZggqPTmqI49tmQvJpBr_jXslq0VU=|1473326342",
" q_c1":"6010b65787864a8fb9ec865b55915c38|1473326342000|1473326342000",
" _za":"dfa112d0-af23-4be3-954e-a683d6ec7723",
" l_cap_id":"ZWEwOTcyYTYxYjY0NDcxOTkzNDgyMmI0NjBiNzM0ZTk=|1474375354|a73ff2da21bfd017330db343bb0684c9dd49d5c4",
" cap_id":"OWU3ZThkODQzZmRhNDkwYmE5ZTRmZjlhZjU4ZDY4MjY=|1474375354|7ac5fffbb3ed8adfa75f1160bbe29d109ea7044a",
" _zap":"e5363c28-3f4f-42cb-bce1-95ff06c2a7e3",
" login":"NDRhZjA1ZDE2ZjA5NDU2MGFkNjVjYWI1ZTU5MWUzZTM=|1474375370|2937e206244e74d68c27b0fc0283d49e2b45e197",
" _xsrf":"a5875b449226a5ec0a36779f705f86ed",
" s-q":"wingide",
" s-i":"20",
" sid":"66krk23v",
" a_t":"2.0ABBMd5UCFwkXAAAATkUPWAAQTHeVAhcJAEDA9KNZggoXAAAAYQJVTcq7CFgA6LP1lnBh4COwooo7iYtjy0woz0rv__Cok8cYOrjpWIu6P__njNRbRg==",
" z_c0":"Mi4wQUJCTWQ1VUNGd2tBUU1EMG8xbUNDaGNBQUFCaEFsVk55cnNJV0FEb3NfV1djR0hnSTdDaWlqdUppMlBMVENqUFNn|1474803790|f17b4edce5fda3aeded37c68a8c57519ef325eb0",
" __utmt":"1",
" __utma":"51854390.732639171.1474791082.1474797902.1474803791.4",
" __utmb":"51854390.2.10.1474803791",
" __utmc":"51854390",
" __utmz":"51854390.1474803791.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic",
" __utmv":"51854390.100-1|2=registration_date=20151201=1^3=entry_date=20151201=1"
}
ZHIHU_HEADER = {
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate, sdch, br",
"Accept-Language":"zh-CN,zh;q=0.8",
"Cache-Control":"max-age=0",
"Connection":"keep-alive",
"Host":"www.zhihu.com",
"Referer":"https://www.baidu.com/link?url=xgQA1RXAuYyPnCNiykbhRBpB_bWVc3_PpO3DGDxhPsu&wd=&eqid=bd13b8af000ac4f00000000357e7b848",
"Upgrade-Insecure-Requests":"1",
"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36'
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihu (+http://www.yourdomain.com)'
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 10
# Obey robots.txt rules
ROBOTSTXT_OBEY = False
ITEM_PIPELINES = {
    'scrapy.pipelines.images.ImagesPipeline':1
}
IMAGES_STORE = 'G:\go'
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihu.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhihu.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'zhihu.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
