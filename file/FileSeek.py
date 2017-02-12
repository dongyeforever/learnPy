# coding = utf-8
import os

f = open('test.txt', 'rb+')
print(f.tell())
print(f.read(3))
print(f.tell())
f.seek(0, os.SEEK_END)
print(f.tell())
f.seek(-5, os.SEEK_CUR)
print(f.tell())
print(f.read())
print(f.tell())

f.close()
