#!/usr/bin/python3
"""THis defines a rectangle
"""


class Rectangle:
    """This is a basic rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializer/COnstructor

        Args:
            width (int): Uses the setter for the property width
            height (int): Samebut with height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """property of width

        Returns:
            int: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter of width

        Args:
            value (int): Sets width to this value

        Raises:
            TypeError: If value is not an int
            ValueError: If value is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property of height

        Returns:
            int: private height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height

        Args:
            value (int): value to be the height

        Raises:
            TypeError: In case value is not an int
            ValueError: In case value is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
