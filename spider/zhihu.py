# coding:utf-8

import requests
from bs4 import BeautifulSoup
import re

s = requests.session()
login_data = {'email': '915026331@qq.com', 'password': '*******', '_xsrf': '3b46957c83dd0c33b7d66091eda77b59'}

# post 登录
requests.post('http://www.zhihu.com/login', login_data)

headers = {
    'Host': 'www.zhihu.com',
    'Origin': 'http://www.zhihu.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.zhihu.com/people/dong-xie-81-67/followers',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
# 验证是否登陆成功，抓取'知乎'首页看看内容
resp = s.get('https://www.zhihu.com/people/dong-xie-81-67/followers', headers=headers)
print(resp.cookies.__str__())
soup = BeautifulSoup(resp.text, 'html.parser')
urls = soup.find_all('a', href=re.compile(r'^/people/'))
for url in urls:
    if 'dong-xie-81-67' not in url['href']:
        print(url.get_text(), url['href'])
        # print(url)
