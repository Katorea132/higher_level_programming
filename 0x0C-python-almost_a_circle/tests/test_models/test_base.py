#!/usr/bin/python3
"""Test module for base functions
"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8
import unittest


class TestBase(unittest.TestCase):
    """Tests for base
    """
    def test_pep8(self):
        """Pep8
        """
        pepi = pep8.StyleGuide(quiet=True)
        res = pepi.check_files(['./models/base.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")
