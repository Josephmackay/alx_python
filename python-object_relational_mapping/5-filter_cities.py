#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

def filter_cities():
    """
    Filter cities by state
    """
    # Check if correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state>".format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Execute SQL query to retrieve cities of the given state
    query = """
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            """
    cursor.execute(query, (state_name,))

    # Fetch all rows and display the results
    result = cursor.fetchall()
    cities = [row[0] for row in result]
    print(", ".join(cities))

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    filter_cities()
