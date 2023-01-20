#!/usr/bin/python3
"""student to json"""


class Student:
    """publice instance attriabutes"""

    def __init__(self, first_name, last_name, age):
        """special method to initialize"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """method that returns directory descriptions"""
        return self.__dict__.copy
