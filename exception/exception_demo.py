# coding: utf-8


try:
    a
except NameError as e:
    print('name error', e)
print('except over')
