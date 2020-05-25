#!/usr/bin/python3
"""defines a Square class
"""


class Square:
    """class that defines Square"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize size and position"""
        self.__size = size
        if not isinstance(position, tuple) or\
           len(position) != 2 or not isinstance(position[0], int)\
           or not isinstance(position[1], int) or position[0] < 0\
           or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """size's getter followed by setter. Properties with both a getter and setter
        should only be documented in their getter method."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be >= 0")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """position's getter followed by setter."""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or\
          len(value) != 2 or not isinstance(value[0], int)\
          or not isinstance(value[1], int) or value[0] < 0\
          or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """  the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #
           f size is equal to 0, print an empty line"""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(0, self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()
