#!/usr/bin/python3
""" class Square that inherits from Rectangle """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ subclass Rectangle """
    def __init__(self, size):
        """ initialize self """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """ returns the area of the square """
        return self.__size ** 2

    def __str__(self):
        """ return """
        return "[Square] <width>/<height>".format(self.__size, self.__size)
