#!/usr/bin/python3
"""Test module for base functions
"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest


class TestBase(unittest.TestCase):
    """Tests for base
    """

    def setUp(self):
        """Resets thingies for the test
        """
        Base._Base__nb_objects = 0

    def test_propperclass(self):
        """Tests for the propper class
        """
        b = Base()
        self.assertTrue(type(b) is Base)
        b = Base(132)
        self.assertTrue(type(b) is Base)

    def test_propperId(self):
        """Tests for the propper ID
        """
        self.assertEqual(Base._Base__nb_objects, 0)
        b = Base()
        self.assertEqual(Base._Base__nb_objects, 1)
        self.assertEqual(b.id, 1)
        b = Base(132)
        self.assertEqual(Base._Base__nb_objects, 1)
        self.assertEqual(b.id, 132)
        b = Base()
        self.assertEqual(Base._Base__nb_objects, 2)
        self.assertEqual(b.id, 2)
        b = Base()
        self.assertEqual(Base._Base__nb_objects, 3)
        self.assertEqual(b.id, 3)
        self.assertEqual(Base._Base__nb_objects, b.id)

    def test_Init(self):
        """Tests for propper initialization
        """
        with self.assertRaises(TypeError) as err:
            Base(1, 2)
        e = "__init__() takes from 1 to 2 positional arguments but 3 \
were given"
        self.assertEqual(str(err.exception), e)
        b = Base("pizza")
        self.assertEqual("pizza", b.id)
        b = Base(id="pizza")
        self.assertEqual("pizza", b.id)

    def test_toJson(self):
        """Tests transformation to a JSON
        """
        test = [{"pizza": 1, "pineapple": 1}]
        self.assertEqual(Base.to_json_string(test),
                         '[{"pizza": 1, "pineapple": 1}]')
        test = [{"pizza": 1, "pineapple": 1}, {"1": 2}]
        self.assertEqual(Base.to_json_string(test),
                         '[{"pizza": 1, "pineapple": 1}, {"1": 2}]')
        test = [{}]
        self.assertEqual(Base.to_json_string(test),
                         '[{}]')
        test = [{}, {}]
        self.assertEqual(Base.to_json_string(test),
                         '[{}, {}]')
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        with self.assertRaises(TypeError) as err:
            Base.to_json_string()
        expect = "to_json_string() missing 1 required positional \
argument: 'list_dictionaries'"
        self.assertEqual(str(err.exception), expect)
