# coding = utf-8

f = open('text.txt', 'w+')
f.write('123')
f.write('这是中文')
f.close()

f = open('text.txt', 'r+')
print(f.encoding)
print(f.read())
