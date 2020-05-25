#!/usr/bin/python3
"""defines a Square class
"""


class Square:
    """class that defines square"""
    def __init__(self, size=0):
        """initializing Square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """  the area of the sqaure"""
        return self.__size ** 2
