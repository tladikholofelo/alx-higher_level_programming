#!/usr/bin/python3
"""A class Square that defines a square by"""


class Square:
    """A class Square

    Attributes:
        size (int): size of the square
    """
    def __init__(self, size=0):
        """Initializes the class Square

        Args:
            size (int): size of the square

        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than 0
        """
        self.__size = size

    def area(self):
        """Calculates the area of the square

        Returns:
            int: The return value. Retunrs the area
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Gets the size of the class instance"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the class instance"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
