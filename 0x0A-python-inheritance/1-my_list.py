#!/usr/bin/python3
"""Defines a list class MyList"""


class MyList(list):
    """A class MyList that inherits from list"""

    def print_sorted(self):
        """Prints a list in sorted ascendding order"""
        print(sorted(self))
