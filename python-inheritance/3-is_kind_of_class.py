#!/usr/bin/python3
"""Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """if the objecclas s that inherited from,"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
