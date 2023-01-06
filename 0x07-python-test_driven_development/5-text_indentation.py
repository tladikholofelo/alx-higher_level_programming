#!/usr/bin/python3
"""A function that prints 2 new lines after the characters ., ? and :"""


def text_indentation(text):
    """Function that prints 2 new lines after ., ? and :

    Args:
        text: input string

    Raises:
        TypeError: if text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d

    print(s[:-3], end="")
