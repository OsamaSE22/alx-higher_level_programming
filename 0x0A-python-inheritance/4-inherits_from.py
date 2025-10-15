#!/usr/bin/python3
"""this module is used to check if an obj is
an instance of a subclass"""


def inherits_from(obj, a_class):
    """return True or False based
    on if the obj is an instance
    of a subclass"""
    if (
            issubclass(type(obj), a_class)
            and not type(obj) is a_class
    ):
        return True
    else:
        False
