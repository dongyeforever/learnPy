# coding: utf-8

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "py_test")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = "select * from user"
count = cursor.execute(sql)
print(count)
print(cursor.rowcount)
print(cursor.rownumber)

rs = cursor.fetchone()
print(rs)
print(cursor.rowcount)
print(cursor.rownumber)

rs = cursor.fetchall()
print(rs)
print(cursor.rowcount)
print(cursor.rownumber)

sql_update = "update user set email='update@qq.com' where id=3"
count = cursor.execute(sql_update)
print(count)
print(cursor.rowcount)

db.commit()
# try:
#     # 执行sql语句
#     cursor.execute(sql)
#     # 提交到数据库执行
#     db.commit()
# except Exception as e:
#     print(e)
#     # 如果发生错误则回滚
#     db.rollback()

# 关闭数据库连接
db.close()
