#!/usr/bin/python3
"""students modules"""


class Student:
    """students clas"""
    def __init__(self, first_name, last_name, age):
        """initilization method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        restriltiociton a dicitionary repressntation of students 
        instance
        """
        dict = vars(self)
        if attrs is None:
            return dict

        studentInfo = {}
        for item in attrs:
            if item in dict:
                studentInfo(item) = dict[item]
        return studentInfo

    def reload_from_json(self, json):
