#!/usr/bin/python3
""" cities name """


import sys
import MySQLdb
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],\
                          passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT cities.name from cities" +
                " INNER JOIN states ON cities.state_id = states.id" +
                " WHERE states.name = %s ORDER BY cities.id ASC", [sys.argv[4]])
    row = cur.fetchall()
    print(", ".join([i[0] for i in row]))
    cur.close()
    db.close()
