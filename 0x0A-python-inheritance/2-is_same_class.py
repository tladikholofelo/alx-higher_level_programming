#!/usr/bin/python3
"""Defines the is_same_class function"""


def is_same_class(obj, a_class):
    """Returns True if object is exactly an instance of the specified class;
    Otherwise, return False"""
    return (type(obj) == a_class)
