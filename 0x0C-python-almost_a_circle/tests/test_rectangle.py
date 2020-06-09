""" module - Rectangle testing """
from models.rectangle import Rectangle
from models.base import Base
import unittest


class TestRectangle(unittest.TestCase):
    """ testing all the methods inside Rectangle class  """
    def Test_create_subclass(self):
        """ testing the creation of class Rectangle that inherits from Base """
        self.assertTrue(issubclass(Rectangle, Base))
        r = Rectangle(10, 2)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)
        r1 = Rectangele(2, 10)
        self.assertIsInstance(r1, Rectangle)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.asserteEqual(r1.id, 2)

