#!/usr/bin/python3
"""
List all states object's id when given the name from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/"
        f"{database_name}",
        pool_pre_ping=True
    )

    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    state = (
            session.query(State).filter(State.name == state_name)
            .order_by(State.id)
            .first()
    )

    # Print the results
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    # Close the session
    session.close()
