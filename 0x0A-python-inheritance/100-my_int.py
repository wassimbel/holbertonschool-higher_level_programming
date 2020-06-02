#!/usr/bin/python3
"""
module - Myint
"""


class MyInt(int):
    """ subclass MyInt """
    def __eq__(self, inv):
        """ inverse instance """
        return int(self) != int(inv)
    def __ne__(self, other):
        """ inverse too """
        return int(self) == int(inv)
