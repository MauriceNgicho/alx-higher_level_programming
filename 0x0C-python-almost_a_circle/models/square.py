#!/usr/bin/python3
"""A square class that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that represents a square and inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the square with size, x, y, and id."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """Get the size of the square (which is the same as width)."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square (affect both width and height)."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes of the square.

        Args:
            *args: No-keyword arguments to update attributes in the order:
                1. id
                2. size (width and height)
                3. x
                4. y
            **kwargs: Keyword arguments to update attributes if *args is empty.
        """
        if args and len(args) > 0:
            attributes = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if i < len(attributes):
                    setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a square."""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
