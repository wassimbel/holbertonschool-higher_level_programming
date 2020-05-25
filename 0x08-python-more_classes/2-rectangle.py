#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """class that defines rectangle"""
    def __init__(self, width=0, height=0):
        """initialize rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """  the area of the square"""
        return self.__height * self.__width

    def perimeter(self):
        """ the perimeter of the rectangle """
        if self.__height == 0 or self.width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2