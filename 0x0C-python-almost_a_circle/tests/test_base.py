#!/usr/bin/python3
""" module - Base testing """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ testing all the methods inside the Base class """
    def Test_create_Base(self):
        """ testing the 1st task creation of Base class """
        nb = Base.__nb_objects
        nb = 0
        self.assertEqual(nb, 0)
        b = Base(1)
        self.assertIsInstance(b, Base)
        self.assertEqual(b.id, 1)
        b = base()
        self.assertEqual(nb, 1)
        self.assertEqual(b.id, 1)
        b = base(None)
        self.assertEqual(nb, 2)
        self.assertEqual(b.id, 2)

    if __name__ == "__main__":
        unittest.main()
