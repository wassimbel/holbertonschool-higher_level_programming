#!/usr/bin/python3
""" module """
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], database=argv[3])
    cur = db.cursor()
    dbname = argv[4]
    cur.execute("""SELECT cities.name FROM cities
                   INNER JOIN states ON cities.state_id = states.id
                   WHERE states.name = %(dbname)s
                   ORDER BY cities.id ASC""", {'dbname': dbname})
    rows = cur.fetchall()
    list = []
    for row in rows:
        list.append(row[0])
    print(', '.join(list))
    cur.close()
    db.close()
