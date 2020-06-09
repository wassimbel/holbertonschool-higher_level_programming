#!/usr/bin/python3
""" module - class Square that inhertis from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ same construction as Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ instantiates self """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ returns private instance attribute """
        return self.width

    @size.setter
    def size(self, val):
        """ sets private instance attribute """
        self.width = val
        self.height = val

    def to_dictionary(self):
        """ returns the dictionary representation of a Square:  """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}

    def __str__(self):
        """ returns Square """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.size))

    def update(self, *args, **kwargs):
        """ assigns a key/value arguments to attributes """
        for count, val in enumerate(args):
            if count == 0:
                self.id = val
            if count == 1:
                self.size = val
            if count == 2:
                self.x = val
            if count == 3:
                self.y = val

        if not args and len(args) == 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
