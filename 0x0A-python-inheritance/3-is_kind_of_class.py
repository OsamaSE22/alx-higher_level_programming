#!/usr/bin/python3
"""this module is used to check if
an object is an instance of a class or subclass"""


def is_kind_of_class(obj, a_class):
    """this func is used to return True or False
    based on if the Obj is instance of a class
    or a subclass"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
