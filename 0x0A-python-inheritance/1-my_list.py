#!/usr/bin/python3
"""this module define a class that inherites from list class and add the
funciton that return sorted list without affecting the original one"""


class MyList(list):
    """this class inherites from list class
    and add some funcitonalities"""
    def print_sorted(self):
        """the method that sorted the list
        without affecting the original one"""

        print(sorted(self))
