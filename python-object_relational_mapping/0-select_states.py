#!/usr/bin/python3
"""imoorting mysqldb """
if __name__== "__main__":
    from sys import argv
    import  MySQLdb
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3])
    cur=db.cursor()
    cur.execute("SELECT id, name FROM states ORDER by states.id ASC")
    rows = cur.fetchall()
    for i  in rows:
        print(i)
    cur.close()
    db.close()
