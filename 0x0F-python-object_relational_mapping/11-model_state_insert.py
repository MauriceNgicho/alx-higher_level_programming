#!/usr/bin/python3
"""
List all states objects from the database
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

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the results
    print(f"{new_state.id}")

    # Close the session
    session.close()
