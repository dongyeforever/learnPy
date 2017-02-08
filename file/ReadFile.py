# encoding = utf-8

f = open('test.txt', 'r')
str = f.read(1024)
print(str)
print(f.fileno())
print(f.mode)
f.close()
