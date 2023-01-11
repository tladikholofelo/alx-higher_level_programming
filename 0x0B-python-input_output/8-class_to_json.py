#!/usr/bin/python3
"""Defines a Python class-to-JSON function class_to_json."""


def class_to_json(obj):
    """Returns the dictionary representation of a simple data structure."""
    return obj.__dict__
