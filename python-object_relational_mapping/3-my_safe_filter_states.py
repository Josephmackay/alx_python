import MySQLdb
import sys

def safe_filter_states_by_name(username, password, database_name, state_name):
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Use a parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    
    # Execute the SQL query with the state name as a parameter
    cursor.execute(query, (state_name,))

    # Fetch all the rows
    states_data = cursor.fetchall()

    # Display the results
    for state in states_data:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Check if all four arguments are provided
    if len(sys.argv) != 5:
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name> <state_name>")
        sys.exit(1)

    # Get MySQL credentials and state name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Call the function to filter states by name safely
    safe_filter_states_by_name(mysql_username, mysql_password, database_name, state_name)
