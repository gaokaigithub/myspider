import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
           "Host": "www.v2ex.com",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Accept - Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
           "Accept - Encoding": "gzip, deflate, br",
           "Referer":"https://www.v2ex.com/signin",
           "Connection": "keep-alive",
           "Upgrade - Insecure - Requests": "1"}

login_url = "https://www.v2ex.com/signin"
vsession = requests.session()
vhtml = vsession.get(login_url,headers = headers).text
vbsj = BeautifulSoup(vhtml,'lxml')

once = vbsj.find("input",{"name":"once"})['value']
u = vbsj.find("input",{"class":"sl"})['name']
p = vbsj.find("input",{"type":"password"})['name']

postdata = {
    u:"xxxx",
    p:"xxxx",
    'once':once,
    'next':"/"
}

vsession.post(login_url,data=postdata,headers = headers)

urltest = "https://www.v2ex.com/go/free"

html = vsession.get(urltest).text
print(html)
