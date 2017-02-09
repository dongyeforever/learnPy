# encoding: utf-8
from collections import Iterable
from functools import reduce


def f(x):
    return x * x


def r(x, y):
    return x * y


m = map(f, range(1, 9))
print(list(m))

r = reduce(r, range(1, 6))
print(r)

l = [1, [1, 2, 3], 2, [1, 2]]
# print([[x * x for x in row] for row in l])
for row in l:
    if isinstance(row, Iterable):
        print(list(map(f, row)))
        # for n in row:
        #     print(f(n))
    elif isinstance(row, int):
        print(f(row))
