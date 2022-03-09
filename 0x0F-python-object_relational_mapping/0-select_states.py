#!/usr/bin/python3
"""
takes 3 arguments: mysql username, mysql password and database name
"""
import sys
import MySQLdb


def main(argv):
    """Connects and lists all states from the database hbtn_0e_0_usa"""
    conn = MySQLdb.connect(host="localhost", port=3306,
    user=argv[1], passwd=argv[2], db=argv[3])

    cur  = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        main(sys.argv)
