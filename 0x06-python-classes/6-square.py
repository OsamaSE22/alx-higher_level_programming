#!/usr/bin/python3
"""this class is named Square.
It as a private attribute called size.
"""


class Square:
    """this is almost an empty class.
    It just has the private attribute size
    it's a part of alx tasks
    """
    def __init__(self, size=0, position=(0, 0)):
        """this is the constructor of this class.
        It's automatically called when an object is created.
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        """this property is to make spaces.
        vertically and horizontally.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value, tuple) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @property
    def size(self):
        """this property to get the value of size.
        without change the value.
        """
        return self.__size

    @size.setter
    def size(self, size):
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

    def my_print(self):
        st = '#'
        sp = ' '
        w = self.__size * st
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in w:
                print((sp * self.__position[0]) + w)
