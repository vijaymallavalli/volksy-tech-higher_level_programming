#!/usr/bin/python3
"""json"""

def save_to_json_file(my_obj, filename):
    """json"""
    with open(filename, "w", encoding="utf=8") as f:
        f.write(my_obj)
        return(len(my-obj))
