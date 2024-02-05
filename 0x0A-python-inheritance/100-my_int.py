#!/usr/bin/python3
"""100-my_int module"""


class MyInt(int):
    """class MyInt that inherits from int
    """
    def __init__(self, value):
        """the class constructor
        Args:
            value: the value passed my the user
        """
        self.value = value

    def __eq__(self, other):
        """Special method __eq__
        Args:
            other: comparator"""
        if isinstance(other, int):
            if self.value == other:
                return False
        elif isinstance(other, myInt):
            return False

    def __ne__(self, other):
        """Special method __ne__"""
        if not self.__eq__(other):
            return True
