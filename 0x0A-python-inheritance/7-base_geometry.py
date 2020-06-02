#!/usr/bin/python3
"""Module for BaseGeometry class
"""


class BaseGeometry():
    """A BaseGeometry class
    """
    def area(self):
        """Area

        Raises:
            Exception: When it's actually not implemented - duh
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates integers

        Args:
            name (string): The name
            value (int): The value

        Raises:
            TypeError: If value is not an int
            ValueError: If value is less or equal than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
