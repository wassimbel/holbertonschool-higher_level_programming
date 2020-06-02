#!/usr/bin/python3
""" module - inherits_from """


def inherits_from(obj, a_class):
    """ Write a function that returns True if the object is an instance of a
        class that inherited (directly or indirectly) from the specified class
        ; otherwise False. """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
