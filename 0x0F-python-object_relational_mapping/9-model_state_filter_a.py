#!/usr/bin/python3
"""
List all states objects that starts with 'a' from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/"
        f"{database_name}",
        pool_pre_ping=True
    )

    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = (
            session.query(State).filter(State.name.like('%a%'))
            .order_by(State.id)
            .all()
    )

    # Print the results
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
