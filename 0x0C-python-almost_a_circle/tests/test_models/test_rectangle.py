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
