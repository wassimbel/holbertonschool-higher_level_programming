""" module - Rectangle testing """
from models.rectangle import Rectangle
from models.base import Base
import unittest


class TestRectangle(unittest.TestCase):
    """ testing all the methods inside Rectangle class  """

    def test_create_subclass(self):
        """ testing the creation of class Rectangle that inherits from Base """
        self.assertTrue(issubclass(Rectangle, Base))
        r = Rectangle(10, 2)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)
        r1 = Rectangle(2, 10)
        self.assertIsInstance(r1, Rectangle)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 2)
        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertIsInstance(r2, Rectangle)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.id, 12)
        del r, r1, r2

    def test_raising_exceptions(self):
        """ testing exceptions and errors """
        with self.assertRaises(TypeError):
            r = Rectangle(10, "2")
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2.1)
        with self.assertRaises(TypeError):
            r = Rectangle(10, True, "")
        with self.assertRaises(TypeError):
            r = Rectangle(10, 10, 1.25)
        with self.assertRaises(TypeError):
            r = Rectangle(10, 10, " ", True, False)
        with self.assertRaises(TypeError):
            r = Rectangle(10, None)
        with self.assertRaises(TypeError):
            r = Rectangle("2", 10, 1, 1, "str")
        with self.assertRaises(TypeError):
            r = Rectangle(2.1, 10, 1, 1.5, 1)
        with self.assertRaises(TypeError):
            r = Rectangle(True, 10, 5, "", 10)
        with self.assertRaises(TypeError):
            r = Rectangle(False, 10)
        with self.assertRaises(ValueError):
            r = Rectangle(10, 0)
        with self.assertRaises(ValueError):
            r = Rectangle(0, 10)
        with self.assertRaises(ValueError):
            r = Rectangle(10, -1)
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 10)
        with self.assertRaises(ValueError):
            r = Rectangle(0, 0)
        with self.assertRaises(ValueError):
            r = Rectangle(-1, -1)
        with self.assertRaises(ValueError):
            r = Rectangle(10, 5, 1, -1)
        with self.assertRaises(ValueError):
            r = Rectangle(10, 6, -2, 1)
        with self.assertRaises(ValueError):
            r = Rectangle(2, 2, -5, -5)
        with self.assertRaises(ValueError):
            r = Rectangle(10, 1, -1, 1, 1)
        with self.assertRaises(ValueError):
            r = Rectangle(10, 4, 1, -1, 10)
        with self.assertRaises(TypeError):
            r = Rectangle()
        with self.assertRaises(TypeError):
            r = Rectangle(10)
        with self.assertRaises(TypeError):
            r = Rectangle(10, 5, 1, 1, 1, 5)

    def test_update_rectangle(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(89, 2)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        r.update(89, 2, 3, 4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)
        del r

    if __name__ == "__main__":
        unittest.main()
