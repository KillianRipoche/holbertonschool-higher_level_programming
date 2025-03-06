#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N) from the database
hbtn_0e_0_usa.
Takes 3 arguments: mysql username, mysql password, and database name.
Usage: ./1-filter_states.py <mysql_username> <mysql_password> <database_name>
"""
import sys
import MySQLdb

if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name)

    cursor = db.cursor()

    query = """
    SELECT *
    FROM states
    WHERE name LIKE BINARY 'N%'
    ORDER BY id ASC;
    """
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
