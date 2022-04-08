#!/usr/bin/python3

from distutils.util import execute
import sys
import MySQLdb


if __name__ == "__main__":
    # opens database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    # prepare a cursor object using cursor() method
    cur = db.cursor()
    state = sys.argv[4]
    # execute SQL query using execute() method.
    query = ("""SELECT * FROM states WHERE name = %s""")
    parameters = (state,)
    cur.execute(query, parameters)
    # Fetch a single row using fetchone() method.
    rows = cur.fetchall()

    for row in rows:
        if row[1] == state:
            print(row)
 
    cur.close()
    db.close()
