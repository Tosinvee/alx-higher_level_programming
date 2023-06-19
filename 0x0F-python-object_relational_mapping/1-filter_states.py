#!/usr/bin/python3
"""
 lists all states with a name starting with N (upper N) from the database

"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.srgv[1],
        passwd=ssys.argv[2],
        db=sys.argv[3],
        port=3306,
        host='localhost')
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
