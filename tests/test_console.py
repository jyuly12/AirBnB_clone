#!/usr/bin/python3
"""This module execute all test to console
"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class Test_Console(unittest.TestCase):
    """This class defines the console tests"""

    def Test_Create(self):
        """Test create a new object"""
        with patch('sys.stdin', StringIO('create\n')) as stdin, patch(
                'sys.stdout', new_callable=StringIO) as stdout:
            HBNBCommand().cmdloop()
            self.assertEqual(stdout.getvalue(), '** class name missing **')
        with patch('sys.stdin', StringIO('create MyModel\n')) as stdin, patch(
                'sys.stdout', new_callable=StringIO) as stdout:
            HBNBCommand().cmdloop()
            self.assertEqual(stdout.getvalue(), '** class doesn\'t exist **')

    def Test_Show(self):
        """Test show command"""
        with patch('sys.stdin', StringIO('show\n')) as stdin, patch(
                'sys.stdout', new_callable=StringIO) as stdout:
            HBNBCommand().cmdloop()
            self.assertEqual(stdout.getvalue(), '** class name missing **')
        with patch('sys.stdin', StringIO('show MyModel\n')) as stdin, patch(
                'sys.stdout', new_callable=StringIO) as stdout:
            HBNBCommand().cmdloop()
            self.assertEqual(stdout.getvalue(), '** class doesn\'t exist **')
        with patch('sys.stdin', StringIO('show BaseModel\n')) as stdin, patch(
                'sys.stdout', new_callable=StringIO) as stdout:
            HBNBCommand().cmdloop()
            self.assertEqual(stdout.getvalue(), '** instance id missing **')
        with patch('sys.stdin', StringIO('show User 123\n')) as stdin, patch(
                'sys.stdout', new_callable=StringIO) as stdout:
            HBNBCommand().cmdloop()
            self.assertEqual(stdout.getvalue(), '** no instance found **')

    def Test_All(self):
        """Test All command"""
        with patch('sys.stdin', StringIO('all MyModel\n')) as stdin, patch(
                'sys.stdout', new_callable=StringIO) as stdout:
            HBNBCommand().cmdloop()
            self.assertEqual(stdout.getvalue(), '** class doesn\'t exist **')

    def Test_Destroy(self):
        """Test Destroy command"""
        with patch(
            'sys.stdin', StringIO('destroy\n')) as stdin, patch(
                'sys.stdout', new_callable=StringIO) as stdout:
            HBNBCommand().cmdloop()
            self.assertEqual(stdout.getvalue(), '** class name missing **')
        with patch(
            'sys.stdin', StringIO('destroy MyModel\n'))as stdin, patch(
                'sys.stdout', new_callable=StringIO) as stdout:
            HBNBCommand().cmdloop()
            self.assertEqual(stdout.getvalue(), '** class doesn\'t exist **')
        with patch(
            'sys.stdin', StringIO('destroy User\n')) as stdin, patch(
                'sys.stdout', new_callable=StringIO) as stdout:
            HBNBCommand().cmdloop()
            self.assertEqual(stdout.getvalue(), '** instance id missing **')
        with patch(
            'sys.stdin', StringIO('destroy User 123\n'))as stdin, patch(
                'sys.stdout', new_callable=StringIO) as stdout:
            HBNBCommand().cmdloop()
            self.assertEqual(stdout.getvalue(), '** no instance found **')

if __name__ == '__main__':
    unittest.main()
