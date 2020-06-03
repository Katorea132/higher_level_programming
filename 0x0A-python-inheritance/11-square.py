#!/usr/bin/python3
"""THis module is for squares
"""
Rekt = __import__("9-rectangle").Rectangle


class Square(Rekt):
    """The square class from the super class rectangle from
    the super class geometry

    Args:
        Rekt (class): super class
    """
    def __init__(self, size):
        """Initializer

        Args:
            size (integer): The size of a side of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area

        Returns:
            int: The area
        """
        return self.__size * self.__size

    def __str__(self):
        """The pretty formated info

        Returns:
            str: The information of the object
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
