import requests
from bs4 import BeautifulSoup
import time
from tkinter import *

def check(domain):
    url = "http://panda.www.net.cn/cgi-bin/check.cgi?area_domain=%s"%domain

    html = requests.get(url)
    bsj = BeautifulSoup(html.text,"lxml")
    num = bsj.find("original").get_text()[:3]
    if num == '210':
        print("%s可以注册"%domain)
    elif num == "213":
        print("查询超时，请重新查询")
    elif num == "211":
        print("%s域名已注册"%domain)
    else:
        print("出现未知问题")
    return num
def shut(domain):
    tk = Tk()
    tk.geometry("300x300")
    m = Message(tk,text = "%s可以注册了"%domain)
    m.pack()
    tk.mainloop()
if __name__ == "__main__":
    d = input('请输入要查询的域名，可输入多个：')
    domains = d.split(',')

    while True:
        for domain in domains:
            num = check(domain)
            if num == '210':
                shut(domain)
                domains.remove(domain)
                break
            time.sleep(1)
