#!/usr/bin/python3

import MySQLdb

conn = MySQLdb.connect(host="localhost", port=3306,\
user="evanz", passwd="signin", db="hbtn_0e_0_usa")

cur  = db.cursor()

cur.execute("SELECT * FROM states WHERE id = 1")

rows = cur.fetchall()

for row in rows:
    print("%s" % col)

print("\n")
