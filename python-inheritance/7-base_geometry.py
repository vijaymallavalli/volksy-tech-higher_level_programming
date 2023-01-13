#!/usr/bin/python3
"""inheritance"""


class BaseGeometry:
    """integer validiataion"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """public instance method"""
        if type(value) is != int:
            raise TypeError("<name> must be an integer")
        if type(value) <= 0:
            raise ValueError("<name> must be greater than 0")
