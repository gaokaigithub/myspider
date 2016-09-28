# myspider
学习爬虫<br>
jike.py  抓取极客学院的课程信息；<br>
domain.py 使用selenium获取查询域名是否已被注册;<br>
test2.py 使用ghost获取查询域名是否已被注册;<br>
test.py 使用qtwebkit获取查询域名是否已被注册，相比还是ghost.py比较简洁。<br>
lg.py 用selenium登陆万网，才发现登陆框在iframe中。<br>
zhihu 使用scrapy获取知乎用户的头像，保存在了本地。<br>
weixin 通过搜狗搜索爬取微信公众号并将获取内容使用mongodb进行保存，不过很容易被ban，只简单地设置了cookie，并且只爬取了关键词的相关搜索结果的一定页数，没有爬取所有结果
