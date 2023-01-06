#!/usr/bin/python3
"""A class LockedClass with no class or object attribute"""


class LockedClass:
    """A class that only creates a new instance attribute first_name"""
    __slots__ = ["first_name"]
