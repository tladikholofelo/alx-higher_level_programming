#!/usr/bin/python3
"""Defines a JSON-to-object function from_json_string."""
import json


def from_json_string(my_str):
    """Returns a Python data structure object represented by a JSON string."""
    return json.loads(my_str)
