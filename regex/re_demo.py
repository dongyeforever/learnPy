# encoding: utf-8

import re


# 找到imooc开头的语句
def find_start(fname):
    f = open(fname)
    for line in f:
        if line.startswith('imooc'):
            print(line)


# 找到imooc开头和结尾的语句
def find_end(fname):
    f = open(fname)
    for line in f:
        if line.startswith('imooc') and line[:-1].endswith('imooc'):
            print(line)


find_start('1.txt')
find_end('1.txt')
print('---------------------')


def find_re(fname, pattern):
    pa = re.compile(pattern)
    f = open(fname)
    for line in f:
        match = pa.match(line)
        if match:
            print(match.group())


find_re('1.txt', r'imooc')
