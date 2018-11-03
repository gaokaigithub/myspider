import  requests
from bs4 import BeautifulSoup
import datetime
import json




headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
           'X-Requested-With':'XMLHttpRequest',
           'Host':'pic.haibao.com',
           'Referer':'http://pic.haibao.com/hotimage/'}

def get_first_id():
    #获取起始skipid
    url = 'http://pic.haibao.com/hotimage/'
    html = requests.get(url,headers=headers).text
    bsj = BeautifulSoup(html, 'lxml')
    input_skip = bsj.find('input', {'name': 'skip'})
    first_id = int(input_skip['value'])
    return first_id


def get_post_url():
    #构造请求url
    t = datetime.datetime.now()
    ct = t.now().ctime()
    y = ct[-5:]
    d = ct.strip(y)
    tt = d[:7]+y+' '+d[8:]+' '+'GMT+0800'+' '+'(中国标准时间)'
    url = 'http://pic.haibao.com/ajax/image:getHotImageList.json?stamp='
    post_url = url+tt
    return post_url

def get_image_urls():
    myurl = get_post_url()
    skip_id = get_first_id()

    url_ids = []
    while 1:
        if skip_id != 1000:
            data = {'skip': skip_id}
            html = requests.post(myurl,headers=headers,data=data).content
            html = html.decode()
            image_content = json.loads(html)
            image_html = image_content['result']
            ids = image_html['ids'].split(',')
            url_ids.extend(ids)
            skip_id = image_html['skip']
            print('正在爬取中，请耐心等待，此时skipid为%s'%skip_id)
        else:
            print('爬取结束')
            break
    urls = ['http://pic.haibao.com/image/%s.html'%i for i in url_ids]
    return urls

if __name__ == '__main__':
    image_urls = get_image_urls()
    print('正在保存链接')
    with open('image_urls.txt','w+') as f:
        for i in image_urls:
            f.write(i+'\n')
        f.close()
    print('保存结束')





