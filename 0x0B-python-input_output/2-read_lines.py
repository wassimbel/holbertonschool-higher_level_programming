#!/usr/bin/python3
""" module - function read_lines """


def read_lines(filename="", nb_lines=0):
    """  function that reads n lines of a text file (UTF8)
        and prints it to stdout  """
    with open(filename, encoding="utf-8") as myfile:
        if nb_lines <= 0:
            print(myfile.read(), end="")
        else:
            for j in range(nb_lines):
                print(myfile.readline(), end="")
