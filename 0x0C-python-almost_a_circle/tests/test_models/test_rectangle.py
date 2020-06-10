#!/usr/bin/python3
"""THis is for tests for rectangles
"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import io
import contextlib
import pep8
import unittest


class TestRectangle(unittest.TestCase):
    """Class to test
    """
    def test_pep8(self):
        """Pep8
        """
        pepi = pep8.StyleGuide(quiet=True)
        res = pepi.check_files(['./models/rectangle.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def setUp(self):
        """Sets up stuff
        """
        Base._Base__nb_objects = 0

    def test_Subclassness(self):
        """Tests if inherited from base
        """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_Init(self):
        """Tests the initializer
        """
        r = Rectangle(1, 2)
        self.assertEqual(r.id, 1)
        with self.assertRaises(TypeError) as err:
            r = Rectangle()
        with self.assertRaises(TypeError) as err:
            r = Rectangle(1)
        with self.assertRaises(TypeError) as err:
            r = Rectangle(1, 3, 2, 4, 5, 6)
        with self.assertRaises(TypeError) as err:
            r = Rectangle("pizza", 1)
        with self.assertRaises(TypeError) as err:
            r = Rectangle(1, "pizza")
        with self.assertRaises(TypeError) as err:
            r = Rectangle(1, 2, "Pizza")
        with self.assertRaises(TypeError) as err:
            r = Rectangle(1, 2, 3, "Pizza")
        with self.assertRaises(ValueError) as err:
            r = Rectangle(-1, 2, 3)
        with self.assertRaises(ValueError) as err:
            r = Rectangle(0, 2, 3)
        with self.assertRaises(ValueError) as err:
            r = Rectangle(1, -2, 3)
        with self.assertRaises(ValueError) as err:
            r = Rectangle(1, 0, 3)
        with self.assertRaises(ValueError) as err:
            r = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError) as err:
            r = Rectangle(1, 2, 3, -4)
        r = Rectangle(width=5, x=6, id=999, y=1, height=100)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.x, 6)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 999)
        self.assertEqual(r.height, 100)
        r.width = 10
        self.assertEqual(r.width, 10)
        r.id = 123123123
        self.assertEqual(r.id, 123123123)
        r.x = 0
        r.y = 0
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_Area(self):
        """this is for the area
        """
        with self.assertRaises(TypeError) as err:
            Rectangle.area()
        r = Rectangle(1, 2)
        self.assertEqual(r.area(), 2)

    def test_Display(self):
        """This is for displaying
        """
        with self.assertRaises(TypeError) as err:
            Rectangle.display()
        r = Rectangle(1, 1)
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            r.display()
        self.assertEqual(out.getvalue(), "#\n")
        r = Rectangle(1, 1, 1, 1)
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            r.display()
        self.assertEqual(out.getvalue(), "\n #\n")

    def test_toStr(self):
        """This is to check str
        """
        with self.assertRaises(TypeError) as err:
            Rectangle.__str__()
        r = Rectangle(1, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
        r = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 1/1 - 1/1")

    def test_Update(self):
        """Tests updates
        """
        with self.assertRaises(TypeError) as err:
            Rectangle.update()
        r = Rectangle(1, 1)
        r.update(132)
        self.assertEqual(r.id, 132)
        r.update(132, 132, 132, 132, 132)
        self.assertEqual(r.width, 132)
        self.assertEqual(r.height, 132)
        self.assertEqual(r.x, 132)
        self.assertEqual(r.y, 132)
        r.update(132, 132, 132, 132, 132, 133)
        self.assertEqual(r.width, 132)
        self.assertEqual(r.height, 132)
        self.assertEqual(r.x, 132)
        self.assertEqual(r.y, 132)
        with self.assertRaises(ValueError):
            r.update(132, -132)
        with self.assertRaises(ValueError):
            r.update(132, 132, -132)
        with self.assertRaises(ValueError):
            r.update(132, 132, 132, -132)
        with self.assertRaises(ValueError):
            r.update(132, 132, 132, 132, -132)
        r.update(id=133)
        self.assertEqual(r.id, 133)
        r.update(id=133, height=133, width=133, x=133, y=133)
        self.assertEqual(r.width, 133)
        self.assertEqual(r.height, 133)
        self.assertEqual(r.x, 133)
        self.assertEqual(r.y, 133)

    def test_toDict(self):
        """Tests to dict function
        """
        with self.assertRaises(TypeError) as err:
            Rectangle.to_dictionary()
        r = Rectangle(1, 1)
        self.assertEqual(r.to_dictionary(),
                         {'width': 1, 'id': 1, 'height': 1, 'x': 0, 'y': 0})
        r = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(r.to_dictionary(),
                         {'width': 1, 'id': 1, 'height': 1, 'x': 1, 'y': 1})
