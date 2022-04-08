#!/usr/bin/python3

from distutils.util import execute
import sys
import pymysql as MySQLdb


if __name__ == "__main__":
    # opens database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd="test", db=sys.argv[3])
    # prepare a cursor object using cursor() method
    cur = db.cursor()
    state = sys.argv[4]
    # execute SQL query using execute() method.
    cur.execute("""SELECT cities.name FROM cities INNER JOIN states on state_id=states.id WHERE states.name = %s ORDER BY cities.id""", state)

    # Fetch a single row using fetchone() method.
    rows = cur.fetchall()

    print(", ".join([row[0] for row in rows]))
 
    cur.close()
    db.close()