#encoding:utf-8

import requests
from lxml import html
#url='https://account.geekbang.org/login?mobile=13411243010'
url='https://account.geekbang.org/account/ticket/login'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
}

data={"country":86,"cellphone":"13411243010","password":"WXdzd781028","captcha":"","remember":1,"platform":3,"appid":1}

proxies = {"http": "http://12.34.56.79:9527"}
sess=requests.session()
sess.post(url,headers=headers,data=data)
response=sess.get("https://time.geekbang.org/column/article/86582")
c=response.text
utf_str=c.encode("ISO-8859-1").decode("utf8")

print(utf_str)