#!/usr/bin/python3
"""python -input"""
import json


def Class_to_json(obj):
    """function that retrns the object"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
