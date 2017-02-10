# encoding: utf-8

# 序列化

import pickle
import json

d = dict(name='Bob', age=20, score=88)
# print(pickle.dumps(d))
f = open('dump.txt', 'wb')

# 序列化
pickle.dump(d, f)

# json
jsonstr = json.dumps(d)

f.close()
print(d)
print(jsonstr)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 80)
print(json.dumps(s, default=lambda obj: obj.__dict__))
