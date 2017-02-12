# coding: utf-8


def f(x):
    assert x != 0, '参数不能为0'

f(0)
raise ValueError('Test Error', 'a')
