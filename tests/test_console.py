#!/usr/bin/python3
"""This module execute all test to console
"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models import storage


class Test_Console(unittest.TestCase):
    """This class defines the console tests"""

    # Test help command
    def test_help(self):
        expected = ("Documented commands (type help <topic>):\n"
                    "========================================\n"
                    "EOF  all  count  create  destroy  help  quit"
                    "show  update")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_help_quit(self):
        expected = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_help_EOF(self):
        expected = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_help_count(self):
        expected = "Counts the number of objects stored in the .json"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(expected, output.getvalue().strip())

    # test create command
    def test_created_class_name_missing(self):
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_created_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Hello"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_created_new(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())

    # test show command
    def test_show_name_missing(self):
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_show_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Hello"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_show_id_missing(self):
        expected = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_show_no_found(self):
        expected = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel 12"))
            self.assertEqual(expected, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.show(\"12\")"))
            self.assertEqual(expected, output.getvalue().strip())

    # test destroy command
    def test_destroy_name_missing(self):
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_destroy_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Hello"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_destroy_id_missing(self):
        expected = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_destroy_no_found(self):
        expected = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 12"))
            self.assertEqual(expected, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy(\"12\")"))
            self.assertEqual(expected, output.getvalue().strip())

    # tests all command
    def test_all_function(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.all()"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())

    def test_all_no_found(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Base"))
            self.assertEqual(expected, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Base.all()"))
            self.assertEqual(expected, output.getvalue().strip())

    # test update command
    def test_update_class_missing(self):
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_update_class_no_found(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Betty"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_update_id_missing(self):
        expected = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_update_id_no_found(self):
        expected = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel 12"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_update_attribute_missing(self):
        expected = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            id_value = output.getvalue().strip()
            test = "update BaseModel {}".format(id_value)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test))
            self.assertEqual(expected, output.getvalue().strip())

    def test_update_value_missing(self):
        expected = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            id_value = output.getvalue().strip()
            test = "update BaseModel {} age".format(id_value)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(test))
            self.assertEqual(expected, output.getvalue().strip())

    # test count command
    def test_count_class_missing(self):
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("count"))
            self.assertEqual(expected, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".count()"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_count_class_value_failed(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("count MyModel"))
            self.assertEqual("0", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.count()"))
            self.assertEqual("0", output.getvalue().strip())

if __name__ == '__main__':
    unittest.main()
