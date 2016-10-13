import requests
from bs4 import BeautifulSoup
from PIL import Image

username = input("请输入用户名： ")
password = input("请输入登陆密码： ")

imgurl = "https://www.zhihu.com/captcha.gif?type=login"
url = "http://www.zhihu.com/login/{0}".format("phone_num")
home = "https://www.zhihu.com"
headers = {
    "Host":"www.zhihu.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding":"gzip, deflate, br",
    "Referer":"https://www.zhihu.com/",
    "Connection":"keep-alive",
    "Upgrade-Insecure-Requests":"1"
}
s = requests.session()
html = s.get(home,headers = headers).text
bsj = BeautifulSoup(html,'lxml')
xsrf = bsj.find("input",{"name":"_xsrf"})['value']

img = s.get(imgurl,headers = headers).content

with open('captcha.gif','wb+') as f:
    f.write(img)
    f.close()
cimg = Image.open('captcha.gif')
cimg.show()
captcha = input("请输入验证码： ")

post_data = {
    "_xsrf":xsrf,
    "password":password,
    "remember_me":"true",
    "phone_num":username,
    "captcha":captcha
}
wer = s.post(url, data=post_data, headers=headers)
if wer.json()["r"] == 0:
    print("登录成功")
else:
    print("登录失败")
    print("错误信息 --->", wer.json()["msg"])
homeurl = "https://www.zhihu.com/"
homepage = s.get(homeurl,headers = headers)
print(homepage.text)



