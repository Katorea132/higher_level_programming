#!/usr/bin/python3
"""THis module contains the class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """This is the subclass Rectangle

    Args:
        Base (class): Super class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializer/Constructor

        Args:
            width (int): width
            height (int): height
            x (int, optional): X. Defaults to 0.
            y (int, optional): Y. Defaults to 0.
            id (int, optional): id. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter of width

        Returns:
            int: width
        """
        return self.__width

    @width.setter
    def width(self, wid):
        """Sets the width

        Args:
            wid (int): Width to set
        """
        self.validator("width", wid, True)
        self.__width = wid

    @property
    def height(self):
        """Getter for height

        Returns:
            int: Height
        """
        return self.__height

    @height.setter
    def height(self, hei):
        """Setter for height

        Args:
            hei (int:) Height
        """
        self.validator("height", hei, True)
        self.__height = hei

    @property
    def x(self):
        """Getter for X

        Returns:
            int: Value of X
        """
        return self.__x

    @x.setter
    def x(self, valx):
        """Setter for X

        Args:
            valx (int): X
        """
        self.validator("x", valx)
        self.__x = valx

    @property
    def y(self):
        """Getter for y

        Returns:
            int: y
        """
        return self.__y

    @y.setter
    def y(self, valy):
        """Setter for y

        Args:
            valy (int): Y
        """
        self.validator("y", valy)
        self.__y = valy

    def validator(self, name, value, equality=False):
        """Validates that the values are in fact integer and either
        bigger than 0 or equal or bigger than 0

        Args:
            name (str): Name of var
            value (int): VAlue to judge
            equality (bool, optional): Defines if the value can
            or not be 0 as minimum. Defaults to False.

        Raises:
            TypeError: [description]
            ValueError: [description]
            ValueError: [description]
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif equality and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """Returns the area

        Returns:
            int: The area
        """
        return self.height * self.width

    def display(self):
        """Prints the rectangle
        """
        print("\n" * self.y, end="")
        print(((" " * self.x) + "#" * self.width + "\n") * (self.height - 1) +
              ((" " * self.x) + self.width * "#"))

    def __str__(self):
        """Prints pretty

        Returns:
            str: The formatted string
        """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates stuff
        """
        if args:
            count = 0
            for val in args:
                if count is 0:
                    self.id = val
                    count += 1
                elif count is 1:
                    self.width = val
                    count += 1
                elif count is 2:
                    self.height = val
                    count += 1
                elif count is 3:
                    self.x = val
                    count += 1
                elif count is 4:
                    self.y = val
                    count += 1
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
