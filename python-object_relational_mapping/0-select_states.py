#!/usr/bin/python3
"""python script"""
import MYSQLdb
import sys


if __name__ == "__main__":
    db = Mysqldb.connect(host="localhost", port=3306, user=argv[1], passwd=-arg[2], db=argv[3])
    cur=db.cursor()
    data=cur.execute("select * from states order by states.id")
    for i in data:
        print(i)
