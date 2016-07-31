import requests
from bs4 import BeautifulSoup
import pandas as pd
names = []
links = []
jian = []
atime = []
nums = []
afree = []
i = 1
while i <95:
    url = "http://www.jikexueyuan.com/course/?pageNum="+str(i)
    try:
        html = requests.get(url).text
    except:
        print("重新抓取")
        continue
    bsj = BeautifulSoup(html,"lxml")
    lesson_infor = bsj.find_all("div",{"class":"lesson-infor"})
    times = bsj.find_all("div",{"class":"timeandicon"})
    frees = bsj.find_all("div",{"class":"lessonimg-box"})
    print("正在采集第%d页"%i)
    i = i+1
    for infor in lesson_infor:
        names.append(infor.find("a").get_text())
        links.append(infor.find("a")['href'])
        jian.append(infor.find("p").get_text())
    for time in times:
        dd = time.find("dd",{"class":"mar-b8"})
        atime.append(dd.find("em").get_text())
        nums.append(time.find("em",{"class":"learn-number"}).get_text())
    for free in frees:
        isfree = free.find("i",{"class":"free-icon"})
        if isfree:
            afree.append("是")
        else:
            afree.append("否")
print("采集结束，开始保存")
info = {"课程名称":names,"课程链接":links,"课程简介":jian,"课程时间":atime,"是否免费":afree,"报名人数":nums}
df = pd.DataFrame(info)
writer = 'course.xlsx'
df.to_excel(writer,sheet_name='jike',encoding='utf-8')
print("保存结束，文件名为%s"%writer)








