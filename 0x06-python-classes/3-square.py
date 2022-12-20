#!/usr/bin/python3
"""A class Square that defines a square"""


class Square:
    """A class Square

    Attributes:
        size (int): size of the square
    """

    def __init__(self, size=0):
        """Initializes the class Square

        Args:
            size (int): the size of the square

        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of the square

        Returns:
            int: The return value. Returns the area
        """
        return self.__size * self.__size
