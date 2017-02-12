# coding: utf-8

import re

' 字符串中相关操作 '

string = 'imooc videonum = 999'

# sub 替换
info = re.sub(r'\d+', '1001', string)

print(info)


def add1(match):
    val = match.group()
    num = int(val) + 1
    return str(num)

info = re.sub(r'\d+', add1, string)
print(info)

# split 分割
string2 = 'imooc:C C++ Java Python'
print(re.split(r':| ', string2))
