#!/usr/bin/python3
"""module that retrns that dictionary descriptions"""


def class_to_json(obj):
    """return the dictionary descriptions of json"""

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
