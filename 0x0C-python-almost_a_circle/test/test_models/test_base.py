#!/usr/bin/python3
"""Unittest for Base class"""
import unittest
from models.base import Base
import json
"""Importing the base and rectangle modules"""


class TestBase(unittest.TestCase):
    """Runs test for the Bases class"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_when_id_is_none(self):
        """Test when id is None"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_with_args(self):
        """Test when argument is passed"""
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

        b2 = Base(123456)
        self.assertEqual(b2.id, 123456)

    def test_with_negative_args(self):
        """Test when negative numbers are passed"""
        b1 = Base(-12)
        self.assertEqual(b1.id, -12)

        b2 = Base(-9)
        self.assertEqual(b2.id, -9)

    def test_with_zero_as_args(self):
        """Test when 0 is passed"""
        b1 = Base(0)
        self.assertEqual(b1.id, 0)

    def test_defualt(self):
        """to check if the unitest is noot running twice"""
        b = Base()
        self.assertEqual(b.id, 1)


class Testto_json_string(unittest.TestCase):
    """Runs test for the Bases class"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_with_valid_args(self):
        """when list is empty"""
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_single_dictionary(self):
        """when only one item is in the list"""
        d = [{
            'id': 100,
            'width': 2,
            'height': 3,
            'x': 4,
            'y': 5
            }]
        result = Base.to_json_string(d)
        expected_result = (
                '[{"id": 100, "width": 2, "height": 3, "x": 4, "y": 5}]'
                )
        self.assertEqual(result, expected_result)

    def test_none_input(self):
        """when None is passed"""
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_empty_dictionary(self):
        """when empty dictionary is passed"""
        data = [{}]
        result = Base.to_json_string(data)
        self.assertEqual(result, "[{}]")

    def test_multiple_dictionaries(self):
        """list of dictionaries"""
        d = [{'width': 2, 'height': 34}, {'width': 9}]
        result = Base.to_json_string(d)
        self.assertEqual(result, '[{"width": 2, "height": 34}, {"width": 9}]')
