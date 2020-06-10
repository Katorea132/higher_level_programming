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

    def test_fromJson(self):
        """Test to test from JSON
        """
        test = '[{"pizza": 1, "pineapple": 1}]'
        self.assertEqual(Base.from_json_string(test),
                         [{"pizza": 1, "pineapple": 1}])
        test = '[{"pizza": 1, "pineapple": 1}, {"1": 2}]'
        self.assertEqual(Base.from_json_string(test),
                         [{"pizza": 1, "pineapple": 1}, {"1": 2}])
        test = '[{}]'
        self.assertEqual(Base.from_json_string(test),
                         [{}])
        test = '[{}, {}]'
        self.assertEqual(Base.from_json_string(test),
                         [{}, {}])
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        with self.assertRaises(TypeError) as err:
            Base.from_json_string()
        expect = "from_json_string() missing 1 required positional \
argument: 'json_string'"
        self.assertEqual(str(err.exception), expect)

    def test_create(self):
        """Tests to test create
        """
        case = Rectangle(1, 3, 2)
        test = Rectangle.create(**(case.to_dictionary()))
        self.assertEqual(str(case), str(test))
        self.assertFalse(case is test)

    def test_toFile(self):
        """Tests to test save
        """
        test = Square(1)
        Square.save_to_file([test])
        testText = [Square.to_json_string(test.to_dictionary())]
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), len(str(testText)) - 2)
        test = Rectangle(1, 3, 2)
        Rectangle.save_to_file([test])
        testText = [Rectangle.to_json_string(test.to_dictionary())]
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), len(str(testText)) - 2)
        test = Square(1)
        Square.save_to_file([test])
        testText = Square.to_json_string(test.to_dictionary())
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), len(str(testText)) + 2)
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        with self.assertRaises(TypeError):
            Base.save_to_file(1)

    def test_loadFrom(self):
        """This tests loads
        """
        test = Square(1)
        testR = Rectangle(1, 1, 1)
        Square.save_to_file([test])
        Rectangle.save_to_file([testR])
        liliS = Square.load_from_file()
        liliR = Rectangle.load_from_file()
        self.assertEqual(str(test), str(liliS[0]))
        self.assertEqual(str(testR), str(liliR[0]))
