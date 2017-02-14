# coding: utf-8

from datetime import datetime

now = datetime.now()
print(now)

# 指定日期和时间
dt = datetime(2015, 4, 19)
print(dt)

# datetime转换timestamp
print(dt.timestamp())

t = 1429372800.0
print(datetime.fromtimestamp(t))

# str转换为datatime
cday = datetime.strptime('2016-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# datatime转换为str
print(now.strftime('%a, %b %d %H:%M'))


