#!/usr/bin/python3
"""Unittest for Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
import io
import os
"""Importing unittest, Base and Rectangle modules"""


class TestRectangleIniheritance(unittest.TestCase):
    """Tests the rectangle class"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_inheritance(self):
        """Check if Rectangle Class is a subclass of Base Class"""
        self.assertTrue(issubclass(Rectangle, Base))


class TestRectangleIdInitialization(unittest.TestCase):
    """Test Rectangle Id Initialization"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_by_passing_hight_and_width(self):
        """Passing only heights and width"""
        r = Rectangle(10, 78)
        self.assertEqual(r.id, 1)

        r1 = Rectangle(10, 5)
        self.assertEqual(r1.id, 2)

        r2 = Rectangle(10, 4, 8, 0, 8)
        self.assertEqual(r2.id, 8)

        r3 = Rectangle(10, 4)
        self.assertEqual(r3.id, 3)


class TestRectangleInitialization(unittest.TestCase):
    """Test Rectangle Initialization"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_by_passing_neg_hight_and_width(self):
        """Passing negative height value"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(-23, 10)

        """Passing 0 width value"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(23, 0)

    def test_by_passing_neg_x_and_y(self):
        """Passing negative x value"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(23, 10, -2)

        """Passing negative y value"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(23, 10, 0, -34)

    def test_by_passing_all_arguments(self):
        """Passing all arguments with id"""
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

        rec = Rectangle(78, 70)
        self.assertEqual(rec.id, 1)

    def test_by_passing_all_neg_arguments(self):
        """Passing all negative arguments with negative id"""
        with self.assertRaises(ValueError):
            r4 = Rectangle(-10, -2, -2, -4, -12)

    def test_invalid_types(self):
        """Testing invalid width type"""
        with self.assertRaises(TypeError):
            r1 = Rectangle("I'm here", (23, 45))

        """Testing invalid height type"""
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, 2.56)

        """Testing invalid x type"""
        with self.assertRaises(TypeError):
            r3 = Rectangle(10, 2, "I'm here")

        """Testing invalid y type"""
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, 2, 5, {'car': 'Tesla'})

    def test_if_None_is_passed(self):
        """Testing None width type"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(None, 2)

        """Testing None height type"""
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, None)

        """Testing None x type"""
        with self.assertRaises(TypeError):
            r3 = Rectangle(10, 2, None)

        """Testing None y type"""
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, 2, 5, None)

    def test_if_Bool_is_passed(self):
        """Testing Boolean width type"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(True, 2)

        """Testing None height type"""
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, False)

        """Testing None x type"""
        with self.assertRaises(TypeError):
            r3 = Rectangle(10, 2, False)

        """Testing None y type"""
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, 2, 5, True)

    def test_init_with_valid_values(self):
        """Test initializing Rectangle with valid values"""
        r = Rectangle(10, 20, 3, 4, 5)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_init_with_default_values(self):
        """Test initializing Rectangle with default values"""
        r = Rectangle(1, 1)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)


class TestRectangleArea(unittest.TestCase):
    """Tests the area of the rectangle"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_valid_area(self):
        """Test if 2 integers are passed"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        self.assertEqual((r1.id), 1)

        """when argumnets are passed"""
        r4 = Rectangle(10, 100, 0, 0, 12)
        self.assertEqual(r4.area(), 1000)

    def test_invalid_area(self):
        """when neative number is passed to width"""
        with self.assertRaises(ValueError):
            r2 = Rectangle(-3, 2)
            r2.area()

        """when negative number is passed to heigth"""
        with self.assertRaises(ValueError):
            r3 = Rectangle(6, -3)
            r3.area()

        with self.assertRaises(ValueError):
            r4 = Rectangle(6, 0)
            r3.area()

        with self.assertRaises(ValueError):
            r5 = Rectangle(0, 0)
            r5.area()


class TestRectangleDisplay(unittest.TestCase):
    """Handles the display of width and height using #"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_valid_display(self):
        """when one is passed as width and height"""
        rec = Rectangle(4, 2)
        expected_output = "####\n####\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rec.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        """when 2 valid arguments are passed"""
        r2 = Rectangle(1, 1)
        expected_output = "#\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r2.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        """when all the arguments are passed"""
        r2 = Rectangle(10, 5, 2, 3, 22)
        expected_output = (
            "\n\n\n  ##########\n  ##########\n  ##########\n  ##########\n"
            "  ##########\n"
        )
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r2.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        """Display a Square"""
        r2 = Rectangle(4, 4)
        expected_output = "####\n####\n####\n####\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r2.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_invalid_display(self):
        """when an invalid argument is passed"""
        with self.assertRaises(TypeError):
            r3 = Rectangle("34", 1)
            r3.display()

        """when an invalid argument is passed to height"""
        with self.assertRaises(TypeError):
            r4 = Rectangle(2, (56, 99))
            r4.display()

        """when 0 is passed as both arguments"""
        with self.assertRaises(ValueError):
            r5 = Rectangle(0, 0)
            r5.display()

        """when 0 is passed as one argument"""
        with self.assertRaises(ValueError):
            r6 = Rectangle(0, 8)
            r6.display()


class TestRectangle__str__(unittest.TestCase):
    """Tests the __str__ special method"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_str_valid_method(self):
        """when all valid args are passed"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        """when y is not passed"""
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

        """when x is not passed"""
        r3 = Rectangle(5, 5, y=1)
        self.assertEqual(str(r3), "[Rectangle] (2) 0/1 - 5/5")

        """when height is not passed"""
        r4 = Rectangle(5, 7)
        self.assertEqual(str(r4), "[Rectangle] (3) 0/0 - 5/7")

    def test_str_invalid_method(self):
        """when width is not passed"""
        with self.assertRaises(ValueError):
            r5 = Rectangle(0, 0, 0, 0, 0)
            str(r5)


class TestRectangleUpdatedDisplay(unittest.TestCase):
    """Test the updated display that handles x and y"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_update_display_with_x_y_valid(self):
        """when valid arguments are passed"""
        r1 = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r1.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        """when zero is passed to one of the coordinates(y)"""
        r2 = Rectangle(3, 2, 1, 0)
        expected_output = " ###\n ###\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r2.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        """when zero is passed to one of the coordinates(x)"""
        r3 = Rectangle(3, 2, 0, 1)
        expected_output = "\n###\n###\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r3.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        """when zero is passed to the coordinates(x & y)"""
        r4 = Rectangle(3, 2, 0, 0)
        expected_output = "###\n###\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r4.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update_display_with_x_y_invalid(self):
        """when zero is passed to all args(x & y)"""
        with self.assertRaises(ValueError):
            r5 = Rectangle(0, 0, 0, 0)
            r5.display()


class TestRectangleUpdateArgs(unittest.TestCase):
    """Test Rectangle Update Args"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_update_args_valid(self):
        """when all args are passed"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, 20, 30, 40, 50)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_update_partial(self):
        """partial update"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, 20)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_updated_args_with_invalid_types(self):
        r = Rectangle(1, 2, 3, 4, 5)
        """when 0 is passed to the updated width and height"""
        with self.assertRaises(ValueError):
            r.update(10, 0, 0)

        """when invalid type is passed to the updated width"""
        with self.assertRaises(TypeError):
            r.update(10, "invalid width", 45)

        """when invalid type is passed to the updated height"""
        with self.assertRaises(TypeError):
            r.update(10, 4, "invalid height")

        """when invalid type is passed to the updated x"""
        with self.assertRaises(TypeError):
            r.update(67, 56, 10, {'key': 'value'})

        """when invalid type is passed to the updated y"""
        with self.assertRaises(TypeError):
            r.update(67, 56, 10, 6, {'key': 'value'})


class TestRectangle_kwargsandargs(unittest.TestCase):
    """Tests the rectangle kwargs and args update"""
    def setUp(self):
        """Reset the id attribute to 0"""
        Base._Base__nb_objects = 0

    def test_if_args_is_called_first(self):
        """args_take_precedence_over_kwargs"""
        r = Rectangle(9, 21, 3, 4, 5)
        r.update(10, width=40)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 9)
        self.assertEqual(r.height, 21)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_when_kwargs_are_passed(self):
        """if only **kwargs are passed"""
        r = Rectangle(10, 10, 10, 10)
        r.update(id=60, width=20, height=30, x=40, y=50)
        self.assertEqual(r.id, 60)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_invalid_kwargs_name(self):
        """when an invalid key is passed"""
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(AttributeError):
            r.update(invalid_attr=10)

    def test_extra_kwargs_name(self):
        """invalid key"""
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(AttributeError):
            r.update(id=10, width=20, height=30, x=40, y=50, extra_attr=60)

    def test_kwargs_skipped_when_args_exist(self):
        """Check that attributes updated by *args have their new values"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, 20, 30, 40, 50, id=60, width=70, height=80, x=90, y=100)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_empty_kwargs(self):
        """when on args are passed"""
        r = Rectangle(2, 3, 4, 5, 9)
        r.update()
        self.assertEqual(r.id, 9)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_some_args_are_given(self):
        """when not args are passed to the update method"""
        r = Rectangle(10, 10, 10, 10)
        r.update(width=40, height=50)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 40)
        self.assertEqual(r.height, 50)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)


class TestRectangle_to_dictionary(unittest.TestCase):
    """Tests the rectangle to_dictionary using valid args"""
    def setUp(self):
        """Reset the id attribute to 0"""
        Base._Base__nb_objects = 0

    def to_dictionary_valid_args(self):
        """when valid arguments are passed"""
        r1 = Rectangle(10, 2, 1, 9)
        expected_dict = {
                'id': 10,
                'width': 2,
                'height': 1,
                'x': 9,
                'y': 0
                }
        self.assertEqual(r1.to_dictionary(), expected_dict)

    def test_to_dictionary_empty(self):
        """Test to_dictionary method for an empty Rectangle"""
        r = Rectangle(1, 1)
        expected_dict = {
            'id': 1,
            'width': 1,
            'height': 1,
            'x': 0,
            'y': 0
            }
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_to_dictionary_with_changes(self):
        """Test to_dictionary method after modifying Rectangle attributes"""
        r = Rectangle(3, 4, 5)
        r.width = 6
        r.height = 7
        expected_dict = {
            'id': 1,
            'width': 6,
            'height': 7,
            'x': 5,
            'y': 0
        }
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_to_dictionary_custom_id(self):
        """Test to_dictionary method with a custom ID"""
        r = Rectangle(2, 3, 4, 5)
        r.id = 100
        expected_dict = {
            'id': 100,
            'width': 2,
            'height': 3,
            'x': 4,
            'y': 5
        }
        self.assertEqual(r.to_dictionary(), expected_dict)


class Test_save_to_file_json_string(unittest.TestCase):
    """Runs test for the Bases class"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

        """Clean up any existing JSON files before each test"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            content = file.read()
            expected_json = (
                '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, '
                '{"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
            )
            self.assertEqual(content, expected_json)

    def test_empty_list_save_to_file(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_None_save_to_file(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_overwrite_existing_file(self):
        """Test that the file is overwritten if it already exists"""
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r])

        # Create a file with some content
        with open("Rectangle.json", "w") as file:
            file.write("existing content")

        r2 = Rectangle(5, 4, 3, 2, 1)
        Rectangle.save_to_file([r2])

        with open("Rectangle.json", "r") as file:
            content = file.read()
            expected_json = (
                    '[{"id": 1, "width": 5, "height": 4, "x": 3, "y": 2}]'
                    )
            self.assertEqual(content, expected_json)

    def tearDown(self):
        """Clean up by removing any created JSON files after each test"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")


class TestDictionaryToStr(unittest.TestCase):
    """Tests the dictionary to str using valid args"""
    def setUp(self):
        """Reset the id attribute to 0"""
        Base._Base__nb_objects = 0

    def dictionary_to_str_valid_args(self):
        """when valid arguments are passed"""
        _dict = [{
            'id': 10,
            'width': 2,
            'height': 1,
            'x': 9,
            'y': 0
            }]
        json_str = Rectangle.to_json_string(_dict)
        expected_dict = '[{"id": 10, "width": 2, "height": 1, "x": 9, "y": 0}]'
        self.assertEqual(json_str, expected_dict)

    def test_dictionary_to_str_empty(self):
        """Test dictionary to str method for an empty Rectangle"""
        _dict = [{
            'id': 1,
            'width': 1,
            'height': 1,
            'x': 0,
            'y': 0
            }]
        json_str = Rectangle.to_json_string(_dict)
        expected_dict = '[{"id": 1, "width": 1, "height": 1, "x": 0, "y": 0}]'
        self.assertEqual(json_str, expected_dict)

    def test_str_to_dictionary_None(self):
        """when None is passed"""
        _dict = None
        json_str = Rectangle.to_json_string(_dict)
        self.assertEqual(json_str, "[]")

    def test_str_to_dictionary_empty(self):
        """when None is passed"""
        _dict = [{}]
        json_str = Rectangle.to_json_string(_dict)
        self.assertEqual(json_str, "[{}]")


class TestDictionary_to_Instance(unittest.TestCase):
    """Runs test for the Bases class"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_dict_to_instance(self):
        """test Dictionary to Instance"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 3/5")

        r1 = Rectangle(4, 6, 2, 1, 12)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r2), "[Rectangle] (12) 2/1 - 4/6")

        """when y is not passed"""
        r2 = Rectangle(5, 5, 1)
        r2_dictionary = r2.to_dictionary()
        r1 = Rectangle.create(**r2_dictionary)
        self.assertEqual(str(r1), "[Rectangle] (4) 1/0 - 5/5")

        """when x is not passed"""
        r1 = Rectangle(5, 5, y=1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Rectangle] (6) 0/1 - 5/5")

        """when height is not passed"""
        r1 = Rectangle(5, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Rectangle] (8) 0/0 - 5/7")


class TestLoadFromFile(unittest.TestCase):
    """Runs test for the Bases class"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

        # Create a test JSON file with example data
        with open("Rectangle.json", "w") as file:
            file.write('[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]')

    def test_load_from_file(self):
        """Call the load_from_file method"""
        rectangles = Rectangle.load_from_file()

        # Check that it returns the expected list of instances
        self.assertEqual(len(rectangles), 1)
        self.assertIsInstance(rectangles[0], Rectangle)
        self.assertEqual(rectangles[0].id, 1)
        self.assertEqual(rectangles[0].width, 10)
        self.assertEqual(rectangles[0].height, 7)
        self.assertEqual(rectangles[0].x, 2)
        self.assertEqual(rectangles[0].y, 8)
