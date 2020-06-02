#!/usr/bin/python3
""" module - function add_attribute """


def add_attribute(object, attribute, value):
    """ adds a new attribute to an object if it’s possible: """

    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(object, attribute, value)
