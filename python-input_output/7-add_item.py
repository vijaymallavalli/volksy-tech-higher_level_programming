#!/usr/bin/python3
"""Load add save"""
import json


def save_to_json_file(my-obj, filename):
    """write a file using json representation"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
