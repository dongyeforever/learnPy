# coding: utf-8

import requests
from bs4 import BeautifulSoup
import re
import pymysql

''' 维基百科首页词条
    https://zh.wikipedia.org/wiki/Wikipedia:首页
'''

url = 'https://en.wikipedia.org/wiki/Main_Page'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
list_urls = soup.find_all('a', href=re.compile(r'^/wiki/'))

conn = pymysql.connect(host="localhost", user="root", password="root", db="py_test", charset="utf8mb4")
try:
    for url in list_urls:
        if not re.search(r'.(jpg|JPG)$', url["href"]):
            print(url.get_text(), '<---->', 'https://en.wikipedia.org' + url['href'])  # 获取会话指针
            with conn.cursor() as cursor:
                sql = "insert into wiki(`urlname`, `urlhref`) VALUES ('%s', '%s') " % (
                    url.get_text(), 'https://en.wikipedia.org' + url['href'])
                cursor.execute(sql)
                conn.commit()
finally:
    conn.close()
