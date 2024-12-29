#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument. Takes four arguments:
MySQL username, MySQL password, database name, and state name searched.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials and the search argument from sys.argv
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to execute queries
    cur = db.cursor()

    # Execute the SQL query to find states with the specified name
    query = (
        "SELECT * FROM states WHERE name LIKE BINARY '{}' "
        "ORDER BY id ASC".format(state_name)
    )
    cur.execute(query)

    # Fetch and print all rows that match the query
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
