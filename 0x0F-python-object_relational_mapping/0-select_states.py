#!/usr/bin/python3

from sys import argv
import MySQLdb

if __name__ == "__main__":
    # opens database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    # prepare a cursor object using cursor() method
    cur = db.cursor()
    # execute SQL query using execute() method.
    cur.execute("SELECT * FROM states")
    
    # Fetch a single row using fetchone() method.
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
