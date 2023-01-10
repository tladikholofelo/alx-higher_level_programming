#!/usr/bin/python3
"""Defines the is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class

    Args:
        obj: the object to check
        a_class (type): the class to match the type of obj to

    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise, return False.
    """
    if isinstance(obj, a_class):
        return True
    return False
