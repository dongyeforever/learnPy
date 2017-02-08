# encoding = utf-8

f = open('test.txt', 'w')
f.write("hahaha")
f.writelines(('1', '2', '3', '\n'))
f.writelines("123456")
f.close()
