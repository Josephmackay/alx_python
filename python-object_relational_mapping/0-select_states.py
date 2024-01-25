import MySQLdb
import sys

def list_states(username, password, database_name):
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to retrieve the list of states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows
    states_data = cursor.fetchall()

    # Display the results
    for state in states_data:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Check if all three arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    # Get MySQL credentials from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Call the function to list states
    list_states(mysql_username, mysql_password, database_name)

