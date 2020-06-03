#!/usr/bin/python3
""" module - function read_lines """


def read_lines(filename="", nb_lines=0):
    """  function that reads n lines of a text file (UTF8)
        and prints it to stdout  """
    with open(filename, encoding="utf-8") as myfile:
        for i in myfile:
            if nb_lines >= len(myfile.readlines()) or nb_lines <= 0:
                print(i, end="")
            else:
                for j in range(nb_lines):
                    print(i, end="")
