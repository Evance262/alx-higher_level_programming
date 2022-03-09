#!/usr/bin/python3
"""
Lits states with a name starting with N (upper N)
from the database hbtn_0e_usa
"""
import sys
import MySQLdb


def main(argv):
    """Connects to a given mysql database"""
    conn = MySQLdb.connect(host="localhost", port="3306",
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
                ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        # cleans up the cursor
        cur.close()
        # closes the database connection
        conn.close()


if __name__ == '__main__':
    if len(sys.argv) == 4:
        main(sys.argv)
