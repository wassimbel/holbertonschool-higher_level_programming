#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """class that defines rectangle"""
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """initialize rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """ defining str """
        str = ""
        if self.__width == 0 or self.__height == 0:
            return str
        str += ("#" * self.__width + "\n") * self.__height
        return str[:-1]

    def __repr__(self):
        """ defining repr """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ defining del """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
