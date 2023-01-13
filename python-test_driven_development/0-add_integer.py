#!/usr/bin/python3
""" 0. Integers addition """


def add_integer(a, b=98):
    """ Function that adds two integers.
    Args:
        a: first integer for addition
        b: second integer for addition
    Returns:
        sum of two integers
    Raises:
        TypeError: if not an int or float
    Doctest Examples:
        see dir: /tests/0-add_integer.txt
    """
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
