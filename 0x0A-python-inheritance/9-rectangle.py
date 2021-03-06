#!/usr/bin/python3
""" module - class Rectangle that inherits from BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ subclass Rectangle """
    def __init__(self, width, height):
        """ initialize self """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ return rectangle area """
        return self.__width * self.__height

    def __str__(self):
        """ return """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
