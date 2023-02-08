#!/usr/bin/python3
"""python script"""
import MYSQLdb
from sys import argv


if __name__ == "__main__":
   mydb = Mysqldb.connect(host="localhost", port=3306, user=argv[1], passwd=-arg[2], db=argv[3])
   mycursor=mydb.cursor()
   mycursor.execute("select * from states order by states.id")
   data=mycursor.fetchall()
   for i in range data:
       print(i)
