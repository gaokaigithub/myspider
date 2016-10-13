import requests
from bs4 import BeautifulSoup
from PIL import Image
import os
import json

class zhihu(object):
    hurl = "https://www.zhihu.com"
    curl = "https://www.zhihu.com/captcha.gif?type=login"
    headers = {
        "Host": "www.zhihu.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.zhihu.com/",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }

    s = requests.session()
    #首先测试cookies是否可以登陆
    def __init__(self):
        if os.path.exists('cookies'):
            print("尝试使用cookies进行登陆")
            self.cookie = self.load_cookie()
            self.s.cookies.update(self.cookie)
            test = self.s.get(self.hurl,headers = self.headers).text
            tbsj = BeautifulSoup(test,'lxml')
            name = tbsj.find("span",{"class":"name"})
            if name:
                print("用户%s已成功登陆"%name.get_text())
            else:
                print("cookies可能过期，尝试使用账号密码进行登陆并更新cookies")
                self.login()
        else:
            print("没有找到cookies，尝试使用账号密码进行登陆并保存cookies")
            self.login()
    #加载cookies
    def load_cookie(self):
        with open("cookies","r") as ocookie:
            cookie = json.load(ocookie)
            return cookie
    #保存cookies
    def save_cookie(self):
        with open("cookies","w") as icookie:
            cook = self.s.cookies.get_dict()
            json.dump(cook,icookie)
            print("已保存cookies")
    #判断邮箱还是手机登陆
    def login_type(self,username):
        if username.isdigit():
            return "phone_num"
        return "email"
    #登陆并保存cookies
    def login(self):
        username = input("请输入用户名： ")
        password = input("请输入登陆密码： ")
        ltype = self.login_type(username)
        html = self.s.get(self.hurl, headers=self.headers).text
        bsj = BeautifulSoup(html, 'lxml')
        xsrf = bsj.find("input", {"name": "_xsrf"})['value']
        img = self.s.get(self.curl, headers=self.headers).content

        with open('captcha.gif', 'wb+') as f:
            f.write(img)
            f.close()
        cimg = Image.open('captcha.gif')
        cimg.show()
        captcha = input("请输入验证码： ")
        post_data = {
            "_xsrf": xsrf,
            "password": password,
            "remember_me": "true",
            ltype: username,
            "captcha": captcha
        }
        url = "http://www.zhihu.com/login/"+ltype
        auo = self.s.post(url, data=post_data, headers=self.headers)
        if auo.json()["r"] == 0:
            print("登录成功")
            self.save_cookie()
        else:
            print("登录失败")
            print("错误信息 --->", auo.json()["msg"])
    #返回已登陆的session
    def get_session(self):
        return self.s

if __name__ == '__main__':
    zhi = zhihu()
    s = zhi.get_session()
    headers = zhi.headers
    url = "https://www.zhihu.com/"
    zhihtml = s.get(url,headers = headers).text
    print(zhihtml)




