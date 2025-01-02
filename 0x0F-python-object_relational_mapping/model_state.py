#!/usr/bin/python3
"""
Defines a State class and links it to the states table in a MySQL database.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# Create the declarative base
Base = declarative_base()


class State(Base):
    """
    State class that links to the MySQL table `states`.
    """
    __tablename__ = 'states'i

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
