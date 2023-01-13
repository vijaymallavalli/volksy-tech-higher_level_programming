#!/usr/bin/python3
"""inheritanceof pypthon classe"""


def inherits_from(obj, a_class):
    """No test cases needed"""
    if type(obj)is a_class or not isinstance(obj, a_class):
        return False
    else:
        return True
