#!/usr/bin/python3
"""Unittest for Square class"""
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
from unittest.mock import patch
import io
import os
"""Importing unittest, Square and Rectangle modules"""


class TestSquareIniheritance(unittest.TestCase):
    """Tests the square class"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_inheritance(self):
        """Check if Square Class is a subclass of Rectangle Class"""
        self.assertTrue(issubclass(Square, Rectangle))


class TestSquareIdInitialization(unittest.TestCase):
    """Test Square Id Initialization"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_by_passing_size(self):
        """Passing only heights and width"""
        s = Square(10)
        self.assertEqual(s.id, 1)

        s1 = Square(10, 5)
        self.assertEqual(s1.id, 2)

        s2 = Square(10, 4, 0, 8)
        self.assertEqual(s2.id, 8)


class TestSquareInitialization(unittest.TestCase):
    """Test Square Initialization"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_by_passing_neg_size(self):
        """Passing negative size value"""
        with self.assertRaises(ValueError):
            s1 = Square(-23)

        """Passing 0 size value"""
        with self.assertRaises(ValueError):
            s1 = Square(0)

    def test_by_passing_neg_x_and_y(self):
        """Passing negative x value"""
        with self.assertRaises(ValueError):
            s1 = Square(23, -10)

        """Passing negative y value"""
        with self.assertRaises(ValueError):
            s1 = Square(23, 10, -34)

    def test_by_passing_all_arguments(self):
        """Passing all arguments with id"""
        s3 = Square(10, 2, 0, 12)
        self.assertEqual(s3.id, 12)

        s = Square(78)
        self.assertEqual(s.id, 1)

    def test_invalid_types(self):
        """Testing invalid width type"""
        with self.assertRaises(TypeError):
            s1 = Square("I'm here", (23, 45))

        """Testing invalid x type"""
        with self.assertRaises(TypeError):
            s3 = Square(10, "I'm here")

        """Testing invalid y type"""
        with self.assertRaises(TypeError):
            s4 = Square(10, 2, {'car': 'Tesla'})

    def test_if_None_is_passed(self):
        """Testing None size type"""
        with self.assertRaises(TypeError):
            s1 = Square(None, 2)

        """Testing None x type"""
        with self.assertRaises(TypeError):
            s3 = Square(10, None)

        """Testing None y type"""
        with self.assertRaises(TypeError):
            s4 = Square(10, 2, None)

    def test_init_with_valid_values(self):
        """Test initializing Rectangle with valid values"""
        s = Square(10, 20, 3, 5)
        self.assertEqual(s.id, 5)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.x, 20)
        self.assertEqual(s.y, 3)


class TestSquareArea(unittest.TestCase):
    """Tests the area of the SquareArea"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_valid_area(self):
        """Test if 1 integers are passed"""
        s1 = Square(3)
        self.assertEqual(s1.area(), 9)
        self.assertEqual((s1.id), 1)

    def test_invalid_area(self):
        """when negative number is passed"""
        with self.assertRaises(ValueError):
            s2 = Square(-3)
            s2.area()

        with self.assertRaises(ValueError):
            s5 = Square(0, 0)
            s5.area()


class TestSquareDisplay(unittest.TestCase):
    """Handles the display of size using #"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_valid_display(self):
        """when one is passed as width and height"""
        s = Square(4)
        expected_output = "####\n####\n####\n####\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            s.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        """when all the arguments are passed"""
        s2 = Square(2, 2, 3, 22)
        expected_output = (
            "\n\n\n  ##\n  ##\n"
            )
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            s2.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_invalid_display(self):
        """when an invalid argument is passed"""
        with self.assertRaises(TypeError):
            s3 = Square("34", 1)
            s3.display()


class TestSquare__str__(unittest.TestCase):
    """Tests the __str__ special method"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_str_valid_method(self):
        """when all valid args are passed"""
        s1 = Square(4, 6, 1, 12)
        self.assertEqual(str(s1), "[Square] (12) 6/1 - 4")

        """when y is not passed"""
        s2 = Square(5, 5)
        self.assertEqual(str(s2), "[Square] (1) 5/0 - 5")

    def test_str_invalid_method(self):
        """when size is not passed"""
        with self.assertRaises(ValueError):
            s5 = Square(0, 0, 0, 0)
            str(s5)


class TestSquareUpdatedDisplay(unittest.TestCase):
    """Test the updated display that handles x and y"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_update_display_with_x_y_valid(self):
        """when valid arguments are passed"""
        s1 = Square(2, 2, 2)
        expected_output = "\n\n  ##\n  ##\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            s1.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        """when zero is passed to the coordinates(x & y)"""
        s4 = Square(3, 0, 0)
        expected_output = "###\n###\n###\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            s4.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update_display_with_x_y_invalid(self):
        """when zero is passed to all args(x & y)"""
        with self.assertRaises(ValueError):
            s5 = Square(0, 0, 0, 0)
            s5.display()


class TestSquareUpdateSize(unittest.TestCase):
    """Test the updated display that handles x and y"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_update_size_with_valid_args(self):
        """passing valid args to size"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 10")

        """when size is 1"""
        s1 = Square(1)
        self.assertEqual(s1.size, 1)
        s1.size = 100
        self.assertEqual(str(s1), "[Square] (2) 0/0 - 100")

    def test_update_size_with_invalid_args(self):
        """passing invalid args to size"""
        with self.assertRaises(TypeError):
            s = Square("10", 20, 30, 40)
            s.size

        """when True is passed to size"""
        with self.assertRaises(TypeError):
            s = Square(True, 20, 30, 40)
            s.size

        """when None is passed to size"""
        with self.assertRaises(TypeError):
            s = Square(None, 20, 30, 40)
            s.size


class TestSquareUpdateArgs(unittest.TestCase):
    """Test Square Update Args"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_update_args_valid(self):
        """when all args are passed"""
        s = Square(1, 2, 3, 4)
        s.update(10, 20, 30, 40)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 20)
        self.assertEqual(s.x, 30)
        self.assertEqual(s.y, 40)

    def test_update_partial(self):
        """partial update"""
        s = Square(1, 2, 3, 4)
        s.update(10, 20)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 20)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_updated_args_with_invalid_types(self):
        s = Square(1, 2, 3, 4)
        """when 0 is passed to the updated width and height"""
        with self.assertRaises(ValueError):
            s.update(10, 0, 0)


class TestSquare_kwargsandargs(unittest.TestCase):
    """Tests the Square kwargs and args update"""
    def setUp(self):
        """Reset the id attribute to 0"""
        Base._Base__nb_objects = 0

    def test_when_kwargs_are_passed(self):
        """if only **kwargs are passed"""
        s = Square(10, 10, 10, 10)
        s.update(id=60, size=20, x=40, y=50)
        self.assertEqual(s.id, 60)
        self.assertEqual(s.size, 20)
        self.assertEqual(s.x, 40)
        self.assertEqual(s.y, 50)

    def test_invalid_kwargs_name(self):
        """when an invalid key is passed"""
        s = Square(1, 2, 4, 5)
        with self.assertRaises(AttributeError):
            s.update(invalid_attr=10)

    def test_extra_kwargs_name(self):
        """invalid key"""
        s = Square(1, 3, 4, 5)
        with self.assertRaises(AttributeError):
            s.update(id=10, size=20, x=40, y=50, extra_attr=60)

    def test_kwargs_skipped_when_args_exist(self):
        """Check that attributes updated by *args have their new values"""
        s = Square(1, 3, 4, 5)
        s.update(10, 20, 40, 50, id=60, size=70,  x=90, y=100)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 20)
        self.assertEqual(s.x, 40)
        self.assertEqual(s.y, 50)

    def test_empty_kwargs(self):
        """when on args are passed"""
        s = Square(2, 4, 5, 9)
        s.update()
        self.assertEqual(s.id, 9)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 5)

    def test_some_args_are_given(self):
        """when not args are passed to the update method"""
        s = Square(10, 10, 10)
        s.update(size=40)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 40)
        self.assertEqual(s.x, 10)
        self.assertEqual(s.y, 10)


class TestSquare_to_dictionary(unittest.TestCase):
    """Tests the Square to_dictionary using valid args"""
    def setUp(self):
        """Reset the id attribute to 0"""
        Base._Base__nb_objects = 0

    def to_dictionary_valid_args(self):
        """when valid arguments are passed"""
        s1 = Square(10, 2, 9)
        expected_dict = {
                'id': 10,
                'size': 2,
                'x': 9,
                'y': 0
                }
        self.assertEqual(r1.to_dictionary(), expected_dict)

    def test_to_dictionary_empty(self):
        """Test to_dictionary method for an empty Rectangle"""
        s = Square(1, 1)
        expected_dict = {
            'id': 1,
            'size': 1,
            'x': 1,
            'y': 0
            }
        self.assertEqual(s.to_dictionary(), expected_dict)

    def test_to_dictionary_with_changes(self):
        """Test to_dictionary method after modifying Rectangle attributes"""
        s = Square(4, 5)
        s.size = 6
        expected_dict = {
            'id': 1,
            'size': 6,
            'x': 5,
            'y': 0
        }
        self.assertEqual(s.to_dictionary(), expected_dict)

    def test_to_dictionary_custom_id(self):
        """Test to_dictionary method with a custom ID"""
        s = Square(2, 4, 5)
        s.id = 100
        expected_dict = {
            'id': 100,
            'size': 2,
            'x': 4,
            'y': 5
        }
        self.assertEqual(s.to_dictionary(), expected_dict)


class Test_save_to_file_json_string(unittest.TestCase):
    """Runs test for the Bases class"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

        """Clean up any existing JSON files before each test"""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_save_to_file(self):
        s1 = Square(10, 2, 8)
        s2 = Square(2, 4)
        Square.save_to_file([s1, s2])

        with open("Square.json", "r") as file:
            content = file.read()
            expected_json = (
                '[{"id": 1, "size": 10, "x": 2, "y": 8}, '
                '{"id": 2, "size": 2, "x": 4, "y": 0}]'
            )
            self.assertEqual(content, expected_json)

    def test_empty_list_save_to_file(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_None_save_to_file(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_overwrite_existing_file(self):
        """Test that the file is overwritten if it already exists"""
        s = Square(1, 2, 3, 5)
        Square.save_to_file([s])

        # Create a file with some content
        with open("Square.json", "w") as file:
            file.write("existing content")

        s2 = Square(5, 3, 2, 1)
        Square.save_to_file([s2])

        with open("Square.json", "r") as file:
            content = file.read()
            expected_json = '[{"id": 1, "size": 5, "x": 3, "y": 2}]'
            self.assertEqual(content, expected_json)

    def tearDown(self):
        """Clean up by removing any created JSON files after each test"""
        if os.path.exists("Square.json"):
            os.remove("Square.json")


class TestDictionaryToStr(unittest.TestCase):
    """Tests the dictionary to str using valid args"""
    def setUp(self):
        """Reset the id attribute to 0"""
        Base._Base__nb_objects = 0

    def dictionary_to_str_valid_args(self):
        """when valid arguments are passed"""
        _dict = [{
            'id': 10,
            'size': 2,
            'x': 9,
            'y': 0
            }]
        json_str = Square.to_json_string(_dict)
        expected_dict = '[{"id": 10, "size": 2, "height": 1, "x": 9, "y": 0}]'
        self.assertEqual(json_str, expected_dict)

    def test_dictionary_to_str_empty(self):
        """Test dictionary to str method for an empty Rectangle"""
        _dict = [{
            'id': 1,
            'size': 1,
            'x': 0,
            'y': 0
            }]
        json_str = Square.to_json_string(_dict)
        expected_dict = '[{"id": 1, "size": 1, "x": 0, "y": 0}]'
        self.assertEqual(json_str, expected_dict)

    def test_str_to_dictionary_None(self):
        """when None is passed"""
        _dict = None
        json_str = Square.to_json_string(_dict)
        self.assertEqual(json_str, "[]")

    def test_str_to_dictionary_empty(self):
        """when None is passed"""
        _dict = [{}]
        json_str = Square.to_json_string(_dict)
        self.assertEqual(json_str, "[{}]")


class TestDictionary_to_Instance(unittest.TestCase):
    """Runs test for the Bases class"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_dict_to_instance(self):
        """test Dictionary to Instance"""
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s2), "[Square] (1) 5/1 - 3")

        s1 = Square(4, 2, 1, 12)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s2), "[Square] (12) 2/1 - 4")

        """when y is not passed"""
        s2 = Square(5, 1)
        s2_dictionary = s2.to_dictionary()
        s1 = Square.create(**s2_dictionary)
        self.assertEqual(str(s1), "[Square] (4) 1/0 - 5")

        """when x is not passed"""
        s1 = Square(5, y=1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), "[Square] (6) 0/1 - 5")

        """when omly size is passed"""
        s1 = Square(5)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), "[Square] (8) 0/0 - 5")


class TestLoadFromFile(unittest.TestCase):
    """Runs test for the Bases class"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

        # Create a test JSON file with example data
        with open("Square.json", "w") as file:
            file.write('[{"id": 1, "size": 10, "x": 2, "y": 8}]')

    def test_load_from_file(self):
        """Call the load_from_file method"""
        squares = Square.load_from_file()

        # Check that it returns the expected list of instances
        self.assertEqual(len(squares), 1)
        self.assertIsInstance(squares[0], Square)
        self.assertEqual(squares[0].id, 1)
        self.assertEqual(squares[0].size, 10)
        self.assertEqual(squares[0].x, 2)
        self.assertEqual(squares[0].y, 8)
