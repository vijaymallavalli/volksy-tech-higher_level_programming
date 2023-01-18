#!/usr/bin/python3
"""writing a name to a file"""


def write_file(filename="", text=""):
    """no file exceptions required"""
    with open(filename, "w", encoding="utf=8") as f:
        f.write(text)
        return len(text)
