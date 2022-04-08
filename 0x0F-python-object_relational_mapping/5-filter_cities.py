#!/usr/bin/python3

from distutils.util import execute
import sys
import MySQLdb


if __name__ == "__main__":
    # opens database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    # prepare a cursor object using cursor() method
    cur = db.cursor()
    # execute SQL query using execute() method.
    cur.execute("""SELECT cities.name
    FROM cities
    JOIN states
    ON state_id=states.id
    WHERE states.name LIKE BINARY %s
    ORDER BY cities.id
    """, (sys.argv[4],))

    # Fetch a single row using fetchone() method.
    rows = cur.fetchall()

    print(", ".join([row[0] for row in rows]))
 
    cur.close()
    db.close()
