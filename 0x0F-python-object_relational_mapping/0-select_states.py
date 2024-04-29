#!/usr/bin/python3
import MySQLdb
import sys
"""
Module to use the DB
"""

db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])

cur = db.cursor()

cur.execute("SELECT * FROM states ORDER BY id ASC")

query_rows = cur.fetchall()
for row in query_rows:
    print(row)

# Close Cursor and Database Connection
cur.close()
db.close()
