#!/usr/bin/python3
"""Unit test for the module City"""

import unittest
from models.city import City
from models import storage


class Test_City(unittest.TestCase):
    """Test for the class City"""
    instance = City()
    instance.state_id = 'Betty'
    instance.name = 'Bogota'

    data_base = storage.all()
    instance_name = 'City.' + instance.id

    def test_cityinit(self):
        """Test for the method __init__"""
        features = self.data_base.get(self.instance_name).to_dict()
        mb = "<class 'models.city.City'>"
        d = "<class 'datetime.datetime'>"

        # Data types
        self.assertEqual(str(type(self.instance)), mb)
        self.assertEqual(str(type(self.instance.id)), "<class 'str'>")
        self.assertEqual(str(type(self.instance.created_at)), d)
        self.assertEqual(str(type(self.instance.updated_at)), d)

        # Basic features storage
        self.assertIn(self.instance_name, self.data_base.keys())
        self.assertIn('created_at', features.keys())
        self.assertIn('updated_at', features.keys())
        self.assertIn('id', features.keys())
        self.assertIn('name', features.keys())
        self.assertIn('state_id', features.keys())

        test_dict = {"id": "fz02d7e0-4254-43b3-b867-d9decb0dda13",
                     "created_at": "2021-06-28T17:47:38.773238",
                     "updated_at": "2021-06-28T17:47:38.773248",
                     "__class__": "City",
                     "state_id": "123",
                     "name": "Bogotá"}

        instance2 = City(**test_dict)

        self.assertIsInstance(instance2, City)
        self.assertEqual(instance2.id, "fz02d7e0-4254-43b3-b867-d9decb0dda13")
        self.assertEqual(instance2.state_id, "123")
        self.assertEqual(instance2.name, "Bogotá")

    def test_citystr(self):
        """Test for the method __str__"""
        cs = '[City] ({}) {}'.format(self.instance.id, self.instance.__dict__)
        my_string = self.instance.__str__()
        self.assertEqual(cs, my_string)

    def test_citysave(self):
        """Test for the method save"""
        dateofupdate = self.instance.updated_at
        self.instance.save()
        new_date = self.instance.updated_at
        self.assertNotEqual(dateofupdate, new_date)

    def test_citytodict(self):
        """Test for the method to_dict"""
        type_of_dict = str(type(self.instance.to_dict()))
        self.assertEqual(type_of_dict, "<class 'dict'>")
        self.assertIn(self.instance_name, self.data_base.keys())

if __name__ == '__main__':
    unittest.main()
