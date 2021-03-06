#!/usr/bin/python3
"""defines a Square class
"""


class Square:
    """class that defines square"""
    def __init__(self, size=0):
        """initializing self"""
        self.__size = size
        """getter"""

    @property
    def size(self):
        return self.__size
    """setter"""

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """  the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """print in stdout the square with the char '#'"""
        if self.size == 0:
            print()
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()
