#!/usr/bin/python3
""" cities name """


from sys import argv
import MySQLdb
if __name__ == "__main__":
    db = MySQLdb.connect(host = "localhost", port =3306, user = sys.argv[1],passwd = sys.argv[2], db = sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities WHERE cities.state_id\
                 IN (SELECT id FROM states WHERE name=%s)\
                 ORDER BY cities.id", [argv[4]])
    row = cur.fetchall()
    print(", ".join(i[0] for i in row))
    cur.close()
    db.close()
