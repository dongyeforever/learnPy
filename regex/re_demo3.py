# coding: utf-8

import re


def match_test(pattern, string):
    m = re.match(pattern, string)
    if m:
        print(m.group())
    else:
        print('未匹配到')


match_test(r'abc|d', 'abcd')
match_test(r'[1-9]?\d$', '100')
match_test(r'[\w]{4,6}@(163|126).com', 'dongye@163.com')
match_test(r'<(\w+>)\w+</\1', '<book>python</book>')  # 分组
match_test(r'<(?P<dongye>\w+>)\w+</(?P=dongye)', '<book>python</book>')  # 引用分组 (?P=name)
