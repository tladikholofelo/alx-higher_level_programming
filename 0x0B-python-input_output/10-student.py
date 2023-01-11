#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """A class Student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets a dictionary representation of the Studen."""
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
