#!/usr/bin/python3
"""Unit test for the module Review"""

import unittest
from models.review import Review
from models import storage


class Test_Review(unittest.TestCase):
    """Test for the class Review"""
    instance = Review()
    instance.place_id = '2886'
    instance.user_id = "User Ana"
    instance.text = "The best hotel"

    data_base = storage.all()
    instance_name = 'Review.' + instance.id

    def test_reviewinit(self):
        """Test for the method __init__"""
        features = self.data_base.get(self.instance_name).to_dict()
        mb = "<class 'models.review.Review'>"
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
        self.assertIn('place_id', features.keys())
        self.assertIn('user_id', features.keys())
        self.assertIn('text', features.keys())

    def test_reviewstr(self):
        """Test for the method __str__"""
        cs = '[Review] ({}) {}'.format(
            self.instance.id, self.instance.__dict__)
        my_string = self.instance.__str__()
        self.assertEqual(cs, my_string)

    def test_reviewsave(self):
        """Test for the method save"""
        dateofupdate = self.instance.updated_at
        self.instance.save()
        new_date = self.instance.updated_at
        self.assertNotEqual(dateofupdate, new_date)

    def test_reviewtodict(self):
        """Test for the method to_dict"""
        type_of_dict = str(type(self.instance.to_dict()))
        self.assertEqual(type_of_dict, "<class 'dict'>")
        self.assertIn(self.instance_name, self.data_base.keys())

if __name__ == '__main__':
    unittest.main()
