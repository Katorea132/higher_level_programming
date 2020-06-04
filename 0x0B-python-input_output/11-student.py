#!/usr/bin/python3
"""Contains the class Student
"""


class Student:
    """THis is the student class :D
    """
    def __init__(self, first_name, last_name, age):
        """Initializer

        Args:
            first_name (str): First name
            last_name (str): Last name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dict method content

        Returns:
            dict: the methods and attributes
        """
        return self.__dict__
