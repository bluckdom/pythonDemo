#coding=utf-8

import pymysql

db = pymysql.connect("localhost","root","root","test")

cursor = db.cursor()

cursor.execute("select * from name")

data  = cursor.fetchall()

for i in data:
    print(i)
db.close()