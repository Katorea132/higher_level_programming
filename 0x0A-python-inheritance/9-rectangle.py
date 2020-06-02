#!/usr/bin/python3
"""Module contains a rectangle class
"""
geo = __import__("7-base_geometry").BaseGeometry


class Rectangle(geo):
    """Rectangle subclass

    Args:
        geo (class): The super class
    """
    def __init__(self, width, height):
        """Initializes the variables width and height previouly checking
        for valid values for them

        Args:
            width (int): Width
            height (int): Height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
