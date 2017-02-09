# encoding: utf-8

str = 'hello, dongye'
for s in str:
    print(s)

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print('%s: %d' % (key, d.get(key)))

for key, val in d.items():
    print(key, "=", val)

g = (x * x for x in range(10))
for n in g:
    print(n)
