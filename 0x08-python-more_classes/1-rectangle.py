#!/usr/bin/python3
"""This module creates a class named Rectangle"""


class Rectangle:
    """A class named Rectangle

    Attributes:
        width (int): width of rectangle
        height (int): height of rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializes the class Rectangle

        Args:
            width: width of the rectangle
            height: height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than 0
        """
        self.width = width
        self.height = height

        @property
        def height(self):
            """Gets the height of the class instance"""
            return self.__height

        @height.setter
        def height(self, value):
            """Sets the height of the class instance"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value

        @property
        def width(self):
            """Gets the width of the class instance"""
            return self.__width

        @width.setter
        def width(self, value):
            """Sets the width of the class instance"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
