#!/usr/bin/python3
"""This module constains a class called Base
"""
import json


class Base:
    """This is the Base class, behold!
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a json formatted out of a dictionary

        Args:
            list_dictionaries (dict): Dictionary

        Returns:
            JSON: JSON formatted string
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @staticmethod
    def from_json_string(json_string):
        """From JSON to string

        Args:
            json_string (JSON str): JSON str

        Returns:
            str: unjsonifies
        """
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """creates

        Returns:
            class: the desired class
        """
        dummy = cls(1, 1) if cls.__name__ is "Rectangle" else cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves to a file

        Args:
            list_objs (list): of objects
        """
        if list_objs:
            dic = [d.to_dictionary() for d in list_objs]
        else:
            dic = []
        with open("{}.json".format(cls.__name__), "w") as f:
            f.write(Base.to_json_string(dic))

    @classmethod
    def load_from_file(cls):
        """Loads from a file and initialized the object

        Returns:
            obj: Object
        """
        try:
            with open(cls.__name__ + ".json", "r") as f:
                return [cls.create(**d) for d in cls.from_json_string(f.read())]
        except:
            return []
