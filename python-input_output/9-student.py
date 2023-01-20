#!/usr/bin/python3
"""student to json"""


class Student:
    """Class to Create student instances"""

    def __init__(self, first_name, last_name, age):
        """json"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """methodjson"""
        return vars(self)
