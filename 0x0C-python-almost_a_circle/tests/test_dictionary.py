""" module - Rectangle testing """
from models.rectangle import Rectangle
from models.base import Base
import unittest


class TestRectangle(unittest.TestCase):
    """ testing all the methods inside Rectangle class  """

    def test_dictionary(self):
        """ testing the dictionary which should returns the dictionary
            representation of a Rectangle """
        r = Rectangle(10, 2, 1, 9)
        r1 = r.to_dictionary()
        dict = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r1, dict)
        del r, r1

    if __name__ == "__main__":
        unittest.main()

