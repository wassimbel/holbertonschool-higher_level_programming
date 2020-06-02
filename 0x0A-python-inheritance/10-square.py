#!/usr/bin/python3
""" module - class Square that inherits from Rectangle """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ subclass Square """
    def __init__(self, size):
        """ initialize self """
        super().integer_validator("size", size)
        super().__init__(size, size)
