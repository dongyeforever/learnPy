# encoding: utf-8

# 反序列化

import pickle

f = open('dump.txt', 'rb')
d = pickle.load(f)
print(d)
