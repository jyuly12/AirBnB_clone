#!/usr/bin/python3
"""Unit test for the module User"""

import unittest
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    """Test for the class User"""
    instance = User()
    data_base = storage.all()
    instance_name = 'User.' + instance.id
    instance.first_name = 'Betty'
    instance.email = "dalisaurito@ternura.com"
    instance.password = "YosoyAurelioCheveroni"
    instance.first_name = "Dali"
    instance.last_name = "Vera"

    def test_userinit(self):
        """Test for the method __init__"""
        features = self.data_base.get(self.instance_name).to_dict()
        mb = "<class 'models.user.User'>"
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
        self.assertIn('first_name', features.keys())
        self.assertIn('email', features.keys())
        self.assertIn('password', features.keys())
        self.assertIn('first_name', features.keys())
        self.assertIn('last_name', features.keys())

        test_dict = {"id": "ff02d7e0-4254-43b3-b867-d9decb0dda13",
                     "created_at": "2021-06-28T17:47:38.773238",
                     "updated_at": "2021-06-28T17:47:38.773248",
                     "__class__": "User",
                     "first_name": "Pepito",
                     "last_name": "Perez",
                     "password": "123456",
                     "email": "dalisaurio@perrito.com"}
        instance2 = User(**test_dict)
        self.assertTrue(isinstance(instance2, User))
        self.assertEqual(instance2.id, "ff02d7e0-4254-43b3-b867-d9decb0dda13")
        self.assertEqual(instance2.first_name, "Pepito")
        self.assertEqual(instance2.last_name, "Perez")
        self.assertEqual(instance2.email, "dalisaurio@perrito.com")
        self.assertEqual(instance2.password, "123456")

    def test_userstr(self):
        """Test for the method __str__"""
        cs = '[User] ({}) {}'.format(self.instance.id, self.instance.__dict__)
        my_string = self.instance.__str__()
        self.assertEqual(cs, my_string)

    def test_usersave(self):
        """Test for the method save"""
        dateofupdate = self.instance.updated_at
        self.instance.save()
        new_date = self.instance.updated_at
        self.assertNotEqual(dateofupdate, new_date)

    def test_usertodict(self):
        """Test for the method to_dict"""
        type_of_dict = str(type(self.instance.to_dict()))
        self.assertEqual(type_of_dict, "<class 'dict'>")
        self.assertIn(self.instance_name, self.data_base.keys())


if __name__ == '__main__':
    unittest.main()
