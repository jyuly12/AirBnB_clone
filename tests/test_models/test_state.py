#!/usr/bin/python3
"""Unit test for the module State"""

import unittest
from models.state import State
from models import storage


class Test_State(unittest.TestCase):
    """Test for the class State"""
    instance = State()
    data_base = storage.all()
    instance_name = 'State.' + instance.id
    instance.name = 'Betty'

    def test_stateinit(self):
        """Test for the method __init__"""
        features = self.data_base.get(self.instance_name).to_dict()
        mb = "<class 'models.state.State'>"
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

        self.instance.last_name = 'Holberton'
        features = self.data_base.get(self.instance_name).to_dict()
        self.assertIn('last_name', features.keys())

        # Extra features storage
        self.instance.perro = 'Dali'
        features = self.data_base.get(self.instance_name).to_dict()
        self.assertEqual(features.get('perro'), 'Dali')

    def test_statestr(self):
        """Test for the method __str__"""
        cs = '[State] ({}) {}'.format(self.instance.id, self.instance.__dict__)
        my_string = self.instance.__str__()
        self.assertEqual(cs, my_string)

    def test_statesave(self):
        """Test for the method save"""
        dateofupdate = self.instance.updated_at
        self.instance.save()
        new_date = self.instance.updated_at
        self.assertNotEqual(dateofupdate, new_date)

    def test_statetodict(self):
        """Test for the method to_dict"""
        type_of_dict = str(type(self.instance.to_dict()))
        self.assertEqual(type_of_dict, "<class 'dict'>")
        self.assertIn(self.instance_name, self.data_base.keys())

if __name__ == '__main__':
    unittest.main()
