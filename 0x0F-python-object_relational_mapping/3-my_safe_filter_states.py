#!/usr/bin/python3
""" module """
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], database=argv[3])
    cur = db.cursor()
    dbname = argv[4]
    cur.execute("""SELECT * from states WHERE name = %(dbname)s
                   ORDER BY id ASC""", {'dbname': dbname})
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
