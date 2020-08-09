#!/usr/bin/python3
""" module """
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], database=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * from states WHERE binary name = '{}'
                   ORDER BY id ASC""".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
