# encoding: utf-8

import re

str1 = 'imooc python'

pattern = re.compile(r'(imooc)')  # r代表元字符串
ma = pattern.match(str1)

ma1 = re.match(r'imooc', str1)

print(ma.group())
print(ma.groups())

print(ma1.group())
