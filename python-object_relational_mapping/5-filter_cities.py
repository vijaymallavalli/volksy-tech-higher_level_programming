#!/usr/bin/python3
"""importing sql fiille to python database"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    sql="SELECT cities.name FROM cities JOIN states ON\
                cities.state_id = state.id \
                WHERE states.name=%s\
                ORDER BY cities.id"
    num_rows=cur.execute(sql,(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
