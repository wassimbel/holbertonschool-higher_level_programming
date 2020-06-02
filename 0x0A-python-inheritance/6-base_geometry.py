#!/usr/bin/python3
""" module - class BaseGeometry """


class BaseGeometry:
    """ class BaseGeometry """
    def area(self):
        """ public instance method that raises an Exception
            with the message area() is not implemented """
        raise Exception("area() is not implemented")
