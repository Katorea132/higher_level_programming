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

    def to_json(self, attrs=None):
        """Returns the dict method content

        Returns:
            dict: the methods and attributes
        """
        if attrs is None:
            return self.__dict__
        else:
            return {l: v for l, v in self.__dict__.items() if l in attrs}

    def reload_from_json(self, json):
        """Updated the dictionary with the given json file

        Args:
            json (dict): The new contents for the dict
        """
        self.__dict__.update(json)
