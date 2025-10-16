#!/usr/bin/python3
"""this module contain a class that raise an exception with a msg """


class BaseGeometry:

    """the class that contain the public method """
    def area(self):

        """a public methid that raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """raise exceptions with false input to this public function"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
