from bs4 import BeautifulSoup
from selenium import webdriver

names = ["dxip","yulj","368377","356377","951195"]
for name in names:
    url = "https://wanwang.aliyun.com/domain/searchresult/?keyword=%s&suffix=.com"%name
    driver = webdriver.Firefox()
    driver.get(url)
    html = driver.page_source
    bsj = BeautifulSoup(html,'lxml')
    info = bsj.find_all("li",{"data-domain":"%s.com"%name})[0]
    com = info.find("a",{"action":"addCart"})
    if com:
        print("可以注册")
    else:
        print("已被注册")

