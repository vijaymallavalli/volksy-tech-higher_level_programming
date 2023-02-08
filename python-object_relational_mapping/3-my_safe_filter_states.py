#!/usr/bin/python3
"""importing sql to pythondatabase"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3,charset="utf8"])
    cur = db.cursor()
    cur.execute(" SELECT * FROM states WHERE name = %s ORDER BY id ASC",[sys.argv[4]])
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
