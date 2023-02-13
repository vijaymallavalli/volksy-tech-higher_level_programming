#!/usr/bin/python3
"""
say_my_name
"""


def print_square(size):
    """
    print a square
    """
    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size == 0:
        return
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
