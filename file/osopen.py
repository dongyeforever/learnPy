# encoding = utf-8

import os

fd = os.open('os_open.txt', os.O_CREAT | os.O_RDWR)
n = os.write(fd, b'imooc')
os.lseek(fd, 0, os.SEEK_SET)

str1 = os.read(fd, 5)
print(str1)

os.close(fd)
