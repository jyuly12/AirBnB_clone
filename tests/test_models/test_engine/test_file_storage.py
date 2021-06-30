#!/usr/bin/python3
"""Unit test for the module User"""
import unittest
import os
from models import storage
from models.base_model import BaseModel


class Test_FileStorage(unittest.TestCase):
    """Test for the class FileStorage"""

    def test_filestorage(self):
        """Test for the method __init__"""
        if os.path.isfile(FileStorage.__file_path):
            os.remove(FileStorage.__file_path)
        all_objs = storage.all()
        # print("-- Reloaded objects --")
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            # print(obj)
            self.assertIsInstance(obj, BaseModel)

        # print("-- Create a new object --")
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model.save()
        # print(my_model)

    def test_all(self):
        """Test for the method all"""
        pass

    def test_new(self):
        """Test for the method new"""
        pass

    def test_save(self):
        """Test for the method save"""
        pass

    def test_reload(self):
        """Test for the method reload"""
        pass


if __name__ == '__main__':
    unittest.main()
