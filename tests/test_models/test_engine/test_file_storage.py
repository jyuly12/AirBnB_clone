#!/usr/bin/python3
"""Unit test for the module User"""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class Test_FileStorage(unittest.TestCase):
    """Test for the class FileStorage"""

    instance1 = FileStorage()
    file = storage._FileStorage__file_path
    storage = FileStorage()

    def test_all(self):
        """Test for the method all()"""
        self.assertIn('all', dir(self.instance1))
        self.assertIsInstance(self.instance1, FileStorage)
        # <class 'models.engine.file_storage.FileStorage'>
        dictt = storage.all()
        self.assertEqual(type(dictt), dict)

    def test_new(self):
        """Test for the method new()"""
        self.assertIn('new', dir(self.instance1))

    def test_save(self):
        """Test for the method save()"""
        self.assertIn('save', dir(self.instance1))
        self.storage.save()
        self.assertTrue(os.path.isfile(self.file))

    def test_save2(self):
        '''Test saving a instances of each type'''
        base = BaseModel()
        storage.new(base)

        user = User()
        storage.new(user)

        state = State()
        storage.new(state)

        place = Place()
        storage.new(place)

        city = City()
        storage.new(city)

        amenity = Amenity()
        storage.new(amenity)

        review = Review()
        storage.new(review)

        storage.save()

        with open(self.file) as f:
            string = f.read()
            self.assertIn("BaseModel." + base.id, string)
            self.assertIn("User." + user.id, string)
            self.assertIn("State." + state.id, string)
            self.assertIn("Place." + place.id, string)
            self.assertIn("City." + city.id, string)
            self.assertIn("Amenity." + amenity.id, string)
            self.assertIn("Review." + review.id, string)

    def test_reload(self):
        """Test for the method reload()"""
        self.assertIn('reload', dir(self.instance1))

        objects = storage.all()

        base = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()

        storage.save()
        storage.reload()

        self.assertIn("BaseModel." + base.id, objects.keys())
        self.assertIn("User." + user.id, objects.keys())
        self.assertIn("State." + state.id, objects.keys())
        self.assertIn("Place." + place.id, objects.keys())
        self.assertIn("City." + city.id, objects.keys())
        self.assertIn("Amenity." + amenity.id, objects.keys())
        self.assertIn("Review." + review.id, objects.keys())


if __name__ == '__main__':
    unittest.main()
