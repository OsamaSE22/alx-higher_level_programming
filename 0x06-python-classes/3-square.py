#!/usr/bin/python3
"""this class is named Square.
It as a private attribute called size.
"""


class Square:
    """this is almost an empty class.
    It just has the private attribute size
    it's a part of alx tasks
    """
    def __init__(self, size=0):
        """this is the constructor of this class.
        It's automatically called when an object is created.
        """
        self.set_size(size)

    def set_size(self, size):
        """this method is to check the input.
        It puts limitations of what kind of input is.
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """this is a public method.
        it returns the area of the square
        """
        area = self.__size ** 2
        return area
