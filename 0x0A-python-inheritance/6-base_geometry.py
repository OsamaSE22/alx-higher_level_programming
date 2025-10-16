#!/usr/bin/python3
"""this module contain a class that raise an exception with a msg """


class BaseGeometry:

    """the class that contain the public method """
    def area(self):

        """a public methid that raise an exception"""
        raise Exception("is not implemented")
