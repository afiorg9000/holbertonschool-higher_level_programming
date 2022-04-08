#!/usr/bin/python3

import sys
import pymysql as MySQLdb

if __name__ == "__main__":
    # opens database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd="test", db=sys.argv[3])
    # prepare a cursor object using cursor() method
    cur = db.cursor()
    # execute SQL query using execute() method.
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id")
    
    # Fetch a single row using fetchone() method.
    rows = cur.fetchall()
    for row in rows:
        print(row)
 
    cur.close()
    db.close()