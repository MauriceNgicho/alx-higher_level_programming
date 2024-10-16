#!/usr/bin/python3
"""
This module defines a class that defines students
"""


class Student:
    """Defines a student by first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of strings representing the
            attribute names to retrieve.

        Returns:
            dict: A dictionary containing the requested attributes.
        """
        if attrs is None:
            return self.__dict__
        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            return {key: value for key,
                    value in self.__dict__.items() if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        from a JSON dictionary.

        Args:
            json (dict): A dictionary with key-value pairs to
            replace attributes.
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
