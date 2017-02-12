# coding: utf-8

import requests


def test_get():
    # header
    headers = {'User-Agent':
                   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    # get请求
    resp = requests.get('https://www.baidu.com', headers=headers)
    # response编码
    resp.encoding = 'utf-8'
    print(resp.text)


def test_post():
    headers = {
        'Origin': 'http://www.thsrc.com.tw',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    playload = {'StartStation': '977abb69-413a-4ccf-a109-0272c24fd490',
                'EndStation': '3301e395-46b8-47aa-aa37-139e15708779',
                'SearchDate': '2017/02/12',
                'SearchTime': '15:00',
                'SearchWay': 'DepartureInMandarin'}
    r = requests.get('http://www.thsrc.com.tw/tw/TimeTable/SearchResult', data=playload, headers=headers)
    print(r)
    print(r.text)


test_get()
test_post()
