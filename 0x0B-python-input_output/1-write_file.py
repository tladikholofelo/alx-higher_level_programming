#!/usr/bin/python3
"""Defines a file-writing function write_file."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8).

    Args:
        filename: name of file
        text: text to write

    Returns:
        The number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
