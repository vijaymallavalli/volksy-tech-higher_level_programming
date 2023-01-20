#!/usr/bin/python3
"""module that define that json represtion"""


class Student:
    """class  to create students ilnstances"""

    def __init__(self, first_name, last_name, age):
        """specia method to inlitialize"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method that treturns directory description"""
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            d_list = {}

            for iatr in range(len(attrs)):
                for satr in obj:
                    if attrs[iatr] == satr:
                        d_list[satr] = obj[satr]
            return d_list

        return obj

