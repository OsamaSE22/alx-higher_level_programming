#!/usr/bin/python3
"""return True if object is an instance of
the specified class"""


def is_same_class(obj, a_class):
    """the func with return the bool value """
    if (
            isinstance(obj, a_class)
            and not issubclass(type(obj), a_class) or type(obj) is a_class
    ):
        return True
    else:
        return False
