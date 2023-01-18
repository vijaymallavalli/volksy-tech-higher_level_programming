#!/usr/bin/python3
"""0-read.md"""


def read_file(filename=""):
    """You are not allowed to import any module"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
