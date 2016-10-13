import requests

cookies = {
    "q_c1": "7deddebdb4214c67a7862f87e48a4d2d|1476252366000|1476252366000",
    " _xsrf": "a65f5ed7ea47bca924da966e8df82ce0",
    " d_c0": "ADBAE4rzrQqPTubkVYCxhSWdqwBpnfapYN0=|1476252367",
    " _zap": "0722087d-690d-4639-a0d4-2510834d89eb",
    " _za": "efa76b5e-31fd-4ec3-9e62-c007883f29fa",
    " __utma": "51854390.1800983773.1476252366.1476252366.1476252366.1",
    " __utmb": "51854390.30.9.1476253688598",
    " __utmc": "51854390",
    " __utmz": "51854390.1476252366.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic",
    " __utmv": "51854390.000--|2=registration_date=20151201=1^3=entry_date=20161012=1",
    " a_t": "2.0ABBMd5UCFwkXAAAAv2glWAAQTHeVAhcJADBAE4rzrQoXAAAAYQJVTb9oJVgAZW2xoS9ZmbGRCb-eiRm_WmW786qHqs5pYS2XlfZHDmfJWcMaKacXYQ==",
    " z_c0": "Mi4wQUJCTWQ1VUNGd2tBTUVBVGl2T3RDaGNBQUFCaEFsVk52MmdsV0FCbGJiR2hMMW1ac1pFSnY1NkpHYjlhWmJ2enFn|1476254655|aa06e73ba0058e140f585126bfae9b78e19886d6",
    " cap_id": "Y2NkNmIzMTA3YWQwNDNkYzhiNzIzNDUyMTZkNmFjZGE=|1476254655|8a74e8a6a31ca42d6ae2f683aad5a86f99f58201",
    " l_cap_id": "MWU0OWZhZjIwNDYzNGY0NmI5Njc0OTQzZTJlZjE3N2E=|1476254655|aa7e1e31bb99d0c7d70709032e5dc48d9c156f91",
    " login": "ODZiMjNiM2YyMWEyNDJjZTk4MTA1YjQyZGUwODc1MTI=|1476254655|dca070d29e9386ea9e16fe380dbc699038bd874c",
    " n_c": "1"
}
cookjar = requests.utils.cookiejar_from_dict(cookies)

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

url = "https://www.zhihu.com/"
s = requests.session()
s.cookies = cookjar
html = s.get(url,headers = headers)

aurl = "https://www.zhihu.com/topic#"
ahtml = s.get(aurl,headers = headers)
print(html.text)