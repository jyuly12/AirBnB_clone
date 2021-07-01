#!/usr/bin/python3
"""Unit test for the class base_model"""

import unittest
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """Test for the class BaseModel"""

    def test_init(self):
        """Test for the method __init__"""
        instance = BaseModel()
        data_base = storage.all()
        instance_name = 'BaseModel.' + instance.id
        features = data_base.get(instance_name).to_dict()
        mb = "<class 'models.base_model.BaseModel'>"
        d = "<class 'datetime.datetime'>"

        # Data types
        self.assertEqual(str(type(instance)), mb)
        self.assertEqual(str(type(instance.id)), "<class 'str'>")
        self.assertEqual(str(type(instance.created_at)), d)
        self.assertEqual(str(type(instance.updated_at)), d)

        # Basic features storage
        self.assertIn(instance_name, data_base.keys())
        self.assertIn('created_at', features.keys())
        self.assertIn('updated_at', features.keys())
        self.assertIn('id', features.keys())

        # Extra features storage
        instance.name = 'Betty'
        instance.last_name = 'Holberton'
        features = data_base.get(instance_name).to_dict()
        self.assertIn('name', features.keys())
        self.assertIn('last_name', features.keys())
        self.assertEqual(features.get('name'), 'Betty')
        self.assertEqual(features.get('last_name'), 'Holberton')

    def test_str(self):
        """Test for the method __str__"""

        instance = BaseModel()
        cs = '[BaseModel] ({}) {}'.format(instance.id, instance.__dict__)
        my_string = instance.__str__()
        self.assertEqual(cs, my_string)

    def test_save(self):
        """Test for the method save"""
        instance = BaseModel()
        data_base = storage.all()
        instance_name = 'BaseModel.' + instance.id

        self.assertIn(instance_name, data_base.keys())

        dateofupdate = instance.updated_at
        instance.save()
        new_date = instance.updated_at

        self.assertNotEqual(dateofupdate, new_date)

    def test_to_dict(self):
        """Test for the method to_dict"""
        instance = BaseModel()
        data_base = storage.all()
        instance_name = 'BaseModel.' + instance.id
        self.assertIn(instance_name, data_base.keys())


if __name__ == '__main__':
    unittest.main()
