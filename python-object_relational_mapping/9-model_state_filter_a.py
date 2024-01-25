#!/usr/bin/python3
"""
Script that lists all State objects containing the letter 'a' from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def filter_states_with_a():
    """
    Fetch all State objects containing the letter 'a' from the database and print them
    """
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the engine and bind it to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database), pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database to get State objects containing the letter 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Print the results
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()

if __name__ == "__main__":
    filter_states_with_a()

