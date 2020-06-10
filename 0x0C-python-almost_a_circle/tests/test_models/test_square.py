#!/usr/bin/python3
"""THis is for tests for rectangles
"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8
import io
import contextlib
import unittest


class TestRectangle(unittest.TestCase):
    """Class to test
    """
    def test_pep8(self):
        """Pep8
        """
        pepi = pep8.StyleGuide(quiet=True)
        res = pepi.check_files(['./models/square.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def setUp(self):
        """Sets up stuff
        """
        Base._Base__nb_objects = 0

    def test_Subclassness(self):
        """Tests if inherited from base
        """
        self.assertTrue(issubclass(Square, Base))

    def test_Init(self):
        """Tests the initializer
        """
        r = Square(1, 2)
        self.assertEqual(r.id, 1)
        with self.assertRaises(TypeError) as err:
            r = Square()
        with self.assertRaises(TypeError) as err:
            r = Square("pizza", 1)
        with self.assertRaises(TypeError) as err:
            r = Square(1, "pizza")
        with self.assertRaises(TypeError) as err:
            r = Square(1, 2, "Pizza")
        with self.assertRaises(ValueError) as err:
            r = Square(-1, 2, 3)
        with self.assertRaises(ValueError) as err:
            r = Square(0, 2, 3)
        with self.assertRaises(ValueError) as err:
            r = Square(1, -2, 3)
        with self.assertRaises(ValueError) as err:
            r = Square(1, 2, -3)
        r = Square(size=1, x=1, y=1, id=1)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.height, 1)
        r.width = 10
        self.assertEqual(r.width, 10)
        r.id = 123123123
        self.assertEqual(r.id, 123123123)
        r.x = 0
        r.y = 0
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        r.size = 5
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 5)

    def test_Area(self):
        """this is for the area
        """
        with self.assertRaises(TypeError) as err:
            Square.area()
        r = Square(2, 2)
        self.assertEqual(r.area(), 4)

    def test_Display(self):
        """This is for displaying
        """
        with self.assertRaises(TypeError) as err:
            Square.display()
        r = Square(1, 1)
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            r.display()
        self.assertEqual(out.getvalue(), " #\n")
        r = Square(1, 1, 1, 1)
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            r.display()
        self.assertEqual(out.getvalue(), "\n #\n")

    def test_toStr(self):
        """This is to check str
        """
        with self.assertRaises(TypeError) as err:
            Square.__str__()
        r = Square(1, 1)
        self.assertEqual(str(r), "[Square] (1) 1/0 - 1")
        r = Square(1, 1, 1, 1)
        self.assertEqual(str(r), "[Square] (1) 1/1 - 1")

    def test_Update(self):
        """Tests updates
        """
        with self.assertRaises(TypeError) as err:
            Square.update()
        r = Square(1, 1)
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
            r.update(132, 132, -132)
        with self.assertRaises(ValueError):
            r.update(132, 132, 132, -132)
        r.update(id=133)
        self.assertEqual(r.id, 133)
        r.update(id=133, height=133, size=133, x=133, y=133)
        self.assertEqual(r.width, 133)
        self.assertEqual(r.height, 133)
        self.assertEqual(r.x, 133)
        self.assertEqual(r.y, 133)

    def test_toDict(self):
        """Tests to dict function
        """
        with self.assertRaises(TypeError) as err:
            Square.to_dictionary()
        r = Square(1, 1)
        self.assertEqual(r.to_dictionary(),
                         {'id': 1, 'size': 1, 'x': 1, 'y': 0})
        r = Square(1, 1, 1, 1)
        self.assertEqual(r.to_dictionary(),
                         {'size': 1, 'id': 1, 'x': 1, 'y': 1})
