__author__ = '38720'
# coding=utf-8
import pymysql



con = pymysql.connect(
    host='192.168.1.211',
    port=3310,
    user='wuzi',
    password='w123456',
    db='wuzi_test',
)

cur = con.cursor()
cur.execute("")
con.commit()
cur.close()
con.close()
