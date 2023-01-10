#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """A class Rectangle that defines a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Intializes a new Rectangle

        Args:
            width (int): the width of the new Rectangle.
            height (int): the height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
