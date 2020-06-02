#!/usr/bin/python3
"""
module - Myint
"""


class MyInt(int):
    """ subclass MyInt """
    def __eq__(self, inv):
        """eq"""
        return not super().__eq__(inv)

    def __ne__(self, inv):
        """not eq"""
        return not super().__ne__(inv)
