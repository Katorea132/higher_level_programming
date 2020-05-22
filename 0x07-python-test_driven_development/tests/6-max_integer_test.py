#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Tests for values the function should handle properly
    """
    def test_numbers(self):
        """Tests for normal values
        """
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([3, 2, 1]), 3)
        self.assertEqual(max_integer([1, 3, 3]), 3)
        self.assertEqual(max_integer([4, 4, 3]), 4)
        self.assertEqual(max_integer([1, 2, 10]), 10)
        self.assertEqual(max_integer([0, -2, -1]), 0)
        self.assertEqual(max_integer([-5, -100, -2]), -2)
        self.assertEqual(max_integer([0, -0, 0]), 0)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([-5]), -5)
        self.assertEqual(max_integer([0.1]), 0.1)
        self.assertEqual(max_integer([0.1, 0.2, -0.1]), 0.2)
        self.assertEqual(max_integer([-5.9, -5.8, -5.4]), -5.4)

    
    def test_oddities(self):
        """Tests for oddities
        """
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer("pizza"), max("pizza"))
        self.assertEqual(max_integer([0, -0, -0.1]), 0)
        self.assertEqual(max_integer([-100, -99.9, -100.1]), -99.9)
        self.assertEqual(max_integer([100.1, 99.9, 100.0]), 100.1)
        self.assertEqual(max_integer([0.000000000000000000000009,
        0.000000000000000000000000000009]), 0.000000000000000000000009)
        self.assertEqual(max_integer([1.0000004, 1.0000008]), 1.0000008)
        self.assertEqual(max_integer("01234567890zZ"), max("01234567890zZ"))
        self.assertEqual(max_integer([[1, 2, 3], [-100]]), \
            max([[1, 2, 3], [-100]]))
        self.assertEqual(max_integer([float('-inf'), float('inf')]),\
            max([float('-inf'), float('inf')]))


    def test_errors(self):
        """This searches for the appropiated raises of errors"
        """
        with self.assertRaises(TypeError):
            max_integer(0)
        with self.assertRaises(TypeError):
            max_integer(True)
        with self.assertRaises(TypeError):
            max_integer(-100)
        with self.assertRaises(TypeError):
            max_integer(100)
