__author__ = '38720'
# coding=utf-8

import pymysql

sqlId = 95437495855000
sqlId = str(sqlId)
sqlTime = "'2017-12-01 01:01:01'"
sqlWord = "UPDATE gt_dispatch_bill SET early_accept_finish_time=" + sqlTime + " WHERE id=" + sqlId

connection = pymysql.connect(
    host='192.168.1.211',
    port=3310,
    user='wuzi',
    password='w123456',
    db='wuzi_test',
)
cur = connection.cursor()
cur.execute(sqlWord)
connection.commit()
cur.close()
connection.close()
