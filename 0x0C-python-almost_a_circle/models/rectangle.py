#!/usr/bin/python3
""" module - subclass Rectangle that inherit from Base """
from models.base import Base


class Rectangle(Base):
    """
    Call the super class with id - this super call with use the logic
    of the __init__ of the Base class.
    Assign each argument width, height, x and y to the right attribute """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ instantiates width, height, x, y, and id """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ returns private instance attribute """
        return self.__width

    @width.setter
    def width(self, val):
        """ sets private instance attribute """
        if type(val) is not int:
            raise TypeError('width must be an integer')
        if val <= 0:
            raise ValueError('width must be > 0')
        self.__width = val

    @property
    def height(self):
        """ returns private instance attribute """
        return self.__height

    @height.setter
    def height(self, val):
        """ sets private instance attribute """
        if type(val) is not int:
            raise TypeError('height must be an integer')
        if val <= 0:
            raise ValueError('height must be > 0')
        self.__height = val

    @property
    def x(self):
        """ returns private instance attribute """
        return self.__x

    @x.setter
    def x(self, val):
        """ sets private instance attribute """
        if type(val) is not int:
            raise TypeError('x must be an integer')
        if val < 0:
            raise ValueError('x must be >= 0')
        self.__x = val

    @property
    def y(self):
        """ returns private instance attribute """
        return self.__y

    @y.setter
    def y(self, val):
        """ sets private instance attribute """
        if type(val) is not int:
            raise TypeError('y must be an integer')
        if val < 0:
            raise ValueError('y must be >= 0')
        self.__y = val

    def area(self):
        """ returns the area value of the Rectangle instance """
        return self.width * self.height

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}

    def display(self):
        """ prints in stdout the Rectangle instance with the character # """
        for x in range(self.__y):
            print()
        for i in range(self.__height):
            print((" " * self.x) + ("#" * self.width))

    def __str__(self):
        """ returns [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ assigns a key/value arguments to attributes """
        for count, val in enumerate(args):
            if count == 0:
                self.id = val
            if count == 1:
                self.width = val
            if count == 2:
                self.height = val
            if count == 3:
                self.x = val
            if count == 4:
                self.y = val

        if not args and len(args) == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle  """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
