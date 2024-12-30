#!/usr/bin/python3
"""
Definition of the City class.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from model_state import Base


class City(Base):
    """
    City class that represents the cities table in the database.

    Attributes:
        id (int): The primary key, auto-incremented, unique identifier.
        name (str): The name of the city, cannot be null.
        state_id (int): Foreign key referencing states.id, cannot be null.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
