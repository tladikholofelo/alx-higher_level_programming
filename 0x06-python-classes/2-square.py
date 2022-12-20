#!/usr/bin/python3
"""A class Square that defines a square"""


class Square:
    """A class Square

    Attributes:
        size (int): size of the square
    """
    def __init__(self, size=0):
        """Initialize the class Square

        Args:
            size (int): size of square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
