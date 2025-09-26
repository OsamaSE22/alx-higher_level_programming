#!/usr/bin/python3
"""
this is a module contain
the definition of rectangle class
>>> r = Rectangle(2, 4)
    >>> print(r.__dict__)
    {'_Rectangle__width': 2, '_Rectangle__height': 4}
    >>> r.width = 10
    >>> r.height = 3
    >>> print(r.__dict__)
    {'_Rectangle__width': 10, '_Rectangle__height': 3}
    >>> r.width = 10
    >>> r.height = 3
    >>> print("Area: {} - Perimeter: {}".format(r.area(), r.perimeter()))
    Area: 30 - Perimeter: 26
    >>> r = Rectangle(2, 4)
    >>> print("Area: {} - Perimeter: {}".format(r.area(), r.perimeter()))
    Area: 8 - Perimeter: 12
    >>> r = Rectangle(2, 4)
    >>> print(str(r))
    ##
    ##
    ##
    ##
"""


class Rectangle:
    """this is a class to define Rectangle.
    """
    def __init__(self, width=0, height=0):
        """this is a constructor to define Rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """this is a property to define width Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """this is a setter to define width Rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """this is a property to define height Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """this is a setter to define height Rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """this is a property to define area Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """this is a property to define perimeter Rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return self.__width * 2 + self.__height * 2

    def __str__(self):
        """ print the rectangle with the character #"""
        symb = '#' * self.__width
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            rect += symb
            if i != self.__height - 1:
                rect += '\n'
        return rect
