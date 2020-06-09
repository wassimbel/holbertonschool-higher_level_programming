#!/usr/bin/python3
""" module - Base testing """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ testing all the methods inside the Base class """
    def test_create_Base(self):
        """ testing the 1st task creation of Base class """
        b = Base(1)
        self.assertIsInstance(b, Base)
        self.assertEqual(b.id, 1)
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base(None)
        self.assertEqual(b.id, 2)
