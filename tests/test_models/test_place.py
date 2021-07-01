#!/usr/bin/python3
"""Unit test for the module Place"""

import unittest
from models.place import Place
from models import storage


class Test_Place(unittest.TestCase):
    """Test for the class Place"""
    instance = Place()
    instance.city_id = "Bogota"
    instance.user_id = "dalisauritobebe"
    instance.name = "DaliHotel"
    instance.description = "El mas bello hotel"
    instance.number_rooms = 1
    instance.number_bathrooms = 1
    instance.max_guest = 10
    instance.price_by_night = 15
    instance.latitude = 8.5
    instance.longitude = 3.1
    instance.amenity_ids = ['cariño', 'comprension', 'ternura']

    data_base = storage.all()
    instance_name = 'Place.' + instance.id

    def test_placeinit(self):
        """Test for the method __init__"""
        features = self.data_base.get(self.instance_name).to_dict()
        mb = "<class 'models.place.Place'>"
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
        self.assertIn('city_id', features.keys())
        self.assertIn('user_id', features.keys())
        self.assertIn('name', features.keys())
        self.assertIn('description', features.keys())
        self.assertIn('number_rooms', features.keys())
        self.assertIn('number_bathrooms', features.keys())
        self.assertIn('max_guest', features.keys())
        self.assertIn('price_by_night', features.keys())
        self.assertIn('latitude', features.keys())
        self.assertIn('longitude', features.keys())
        self.assertIn('amenity_ids', features.keys())

        test_dict = {"id": "fz02d7e0-4254-43b3-b867-d9decb0dda13",
                     "created_at": "2021-06-28T17:47:38.773238",
                     "updated_at": "2021-06-28T17:47:38.773248",
                     "__class__": "Place",
                     "city_id": "123Bog",
                     "user_id": "Dali1",
                     "name": "Dalisaurito",
                     "description": "Hotel",
                     "number_rooms": "8",
                     "number_bathrooms": "3",
                     "max_guest": "300",
                     "price_by_night": "100",
                     "latitude": "123",
                     "longitude": "456",
                     "amenity_ids": "Comprension y Ternura"}

        instance2 = Place(**test_dict)

        self.assertIsInstance(instance2, Place)
        self.assertEqual(instance2.id, "fz02d7e0-4254-43b3-b867-d9decb0dda13")
        self.assertEqual(instance2.city_id, "123Bog")
        self.assertEqual(instance2.user_id, "Dali1")
        self.assertEqual(instance2.name, "Dalisaurito")
        self.assertEqual(instance2.description, "Hotel")
        self.assertEqual(instance2.number_rooms, "8")
        self.assertEqual(instance2.number_bathrooms, "3")
        self.assertEqual(instance2.max_guest, "300")
        self.assertEqual(instance2.price_by_night, "100")
        self.assertEqual(instance2.latitude, "123")
        self.assertEqual(instance2.longitude, "456")
        self.assertEqual(instance2.amenity_ids, "Comprension y Ternura")

    def test_placestr(self):
        """Test for the method __str__"""
        cs = '[Place] ({}) {}'.format(self.instance.id, self.instance.__dict__)
        my_string = self.instance.__str__()
        self.assertEqual(cs, my_string)

    def test_placesave(self):
        """Test for the method save"""
        dateofupdate = self.instance.updated_at
        self.instance.save()
        new_date = self.instance.updated_at
        self.assertNotEqual(dateofupdate, new_date)

    def test_placetodict(self):
        """Test for the method to_dict"""
        type_of_dict = str(type(self.instance.to_dict()))
        self.assertEqual(type_of_dict, "<class 'dict'>")
        self.assertIn(self.instance_name, self.data_base.keys())


if __name__ == '__main__':
    unittest.main()
