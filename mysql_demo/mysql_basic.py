# encoding=utf-8
import mysql.connector
import pymysql

try:
    conn = mysql.connect(host='localhost', port=3306, db='test1', user='root', passwd='mysql_demo', charset='utf8')
    cs1 = conn.cursor()
    count = cs1.execute("update students set sname='刘邦' where id=6")
    print(count)
    conn.commit()
    cs1.close()
    conn.close()
except Exception as e:
    print(e.message)
