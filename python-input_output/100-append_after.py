#!/usr/bin/python3
#100-append_after.py
"""defines a  text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """insert text after each lilne containing a given string in a file."""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text +=  new_string
    with open(filename,"w") as w:
        w.write(text)
