__author__ = '38720'
# coding=utf-8

import pymysql

# 链接数据库

connection = pymysql.connect(
    host='192.168.1.211',
    port=3310,
    user='wuzi',
    password='w123456',
    db='wuzi_test',
)

# 获取操作游标
cur = connection.cursor()
sqlId = 95437495855000
sqlId = str(sqlId)
print(type(sqlId))
sqlTime = "'2017-12-02 10:10:10'"
liststr = "INSERT "
print(type(liststr))
cur.execute(liststr)
connection.commit()
results = cur.fetchall()
print(results)
cur.close()
connection.close()
