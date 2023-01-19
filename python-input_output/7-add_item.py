#!/usr/bin/python3
"""Load add save"""
import json


def save_to_json_file(my_obj, filename):
    """write a file using json representation"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
