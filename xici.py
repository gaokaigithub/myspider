import requests
from bs4 import BeautifulSoup
import pymysql
import time

def get_ip():
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36'}
    iplist = []
    for i in range(1,11):
        url = 'http://www.xicidaili.com/nn/'+str(i)
        time.sleep(5)
        html = requests.get(url,headers = headers).text
        bsj = BeautifulSoup(html,'lxml')
        ipss = bsj.find_all('tr',{'class':'odd'})
        for ips in ipss:
            ipe = ips.find_all('td')
            ip = ipe[1].get_text()
            port = ipe[2].get_text()
            ipw = 'http://' +ip + ':' + port
            iplist.append(ipw)
    return iplist

def save_ip():
    iplist = get_ip()
    conn = pymysql.connect(host = '127.0.0.1',port = 3306,user = 'root',password = 'xxxxx',db = 'ip')
    cur = conn.cursor()
    cur.execute('create table if not exists ip(ip varchar(255))')
    for ip in iplist:
        cur.execute('insert into ip values(%s)',ip)
        conn.commit()
if __name__ == '__main__':
    save_ip()
