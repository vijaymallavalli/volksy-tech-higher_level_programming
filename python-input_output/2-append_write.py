#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """returns a file"""
    with open(filename, "a", encoding="utf=8") as f:
        f.write(text)
        return(len(text))
