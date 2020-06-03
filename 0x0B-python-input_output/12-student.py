#!/usr/bin/python3
""" module - class Student """


class Student():
    """ class Student that defines a student """

    def __init__(self, first_name, last_name, age):
        """ initialize self """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary  """
        list = {}
        if hasattr(self, '__dict__') and isinstance(attrs, list):
            for i in attrs:
                if isinstance(i, str):
                    list[i] = self.__dict__[i]
            return list
        return self.__dict__
