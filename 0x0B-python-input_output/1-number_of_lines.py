#!/usr/bin/python3
""" module - function number_of_lines_ """


def number_of_lines(filename=""):
    """ function that returns the number of lines of a text file """
    nb = 0
    with open(filename, encoding="utf-8") as myfile:
        for i in myfile:
            nb += 1
        return nb
