#!/usr/bin/python3
"""
Module to use the DB
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states")

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
