#!/usr/bin/python3
"""
Base class module
"""
import json
import os


class Base:
    """Base class to manage 'id' attribute in all future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for Base class
        Args:
            id (int): Optional; id to be assigned to the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # Static method to convert a list of dictionaries to a JSON string
    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        list_dicts = []

        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]

        json_string = cls.to_json_string(list_dicts)

        # Open the file in write mode and overwrite with the JSON string
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of dictionaries from a JSON string."""
        if json_string is None or len(json_string.strip()) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with attributes set from dictionary."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Dummy Rectangle with width=1, height=1
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Dummy Square with size=1
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file."""
        filename = cls.__name__ + ".json"

        # Check if the file exists and return an empty list if it doesn't
        if not os.path.exists(filename):
            return []

        # Read the file content
        with open(filename, 'r') as file:
            json_string = file.read()

        # Convert the JSON string to a list of dictionaries
        list_dicts = cls.from_json_string(json_string)

        # Create a list of instances from the list of dictionaries
        list_instances = [cls.create(**dictionary)
                          for dictionary in list_dicts]

        return list_instances
