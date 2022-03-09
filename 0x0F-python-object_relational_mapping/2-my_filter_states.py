#!/usr/bin/python3
"""
Lits states with a name starting with N (upper N) from
the database hbtn_0e_usa
"""
import sys
import MySQLdb


def main(argv):
    """Connects to a given mysql database"""
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}%'\
                ORDER BY id ASC".format(argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    pass
    # cleans up the cursor
    cur.close()
    # closes the database connection
    conn.close()


if __name__ == '__main__':
    if len(sys.argv) == 5:
        main(sys.argv)
