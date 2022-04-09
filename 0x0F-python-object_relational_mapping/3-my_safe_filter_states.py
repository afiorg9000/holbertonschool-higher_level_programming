#!/usr/bin/python3

"""
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""
from distutils.util import execute
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    state = sys.argv[4]
    query = ("""SELECT * FROM states WHERE name = %s""")
    parameters = (state,)
    cur.execute(query, parameters)
    rows = cur.fetchall()
    for row in rows:
        if row[1] == state:
            print(row)
    cur.close()
    db.close()
