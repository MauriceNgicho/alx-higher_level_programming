#!/usr/bin/python3
"""
Lists all cities of a state from the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Get arguments
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

    # Create a cursor
    cur = db.cursor()

    # Execute the query safely to avoid SQL injection
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;
    """
    cur.execute(query, (state_name,))

    # Fetch all the results
    rows = cur.fetchall()

    # Print the results as a comma-separated string
    print(", ".join([row[0] for row in rows]))

    # Close the cursor and database connection
    cur.close()
    db.close()
