#!/usr/bin/python3
# unit test for base.py script

import unittest  # allows to assert and test
import os  # allows to run bash commands

# scripts to test:
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key,
          type(my_model_json[key]), my_model_json[key]))


# class Test_Base(unittest.TestCase):
#     # class to test the unit models.base_model.py

#     def test_basemodel(self):
#         # test for class BaseModel

#         a = BaseModel()

#         self.assertEqual(a.id, 1)
#         self.assertEqual(b.id, 2)
#         self.assertEqual(c.id, 3)
#         self.assertEqual(d.id, 12)
#         self.assertEqual(e.id, 4)

#         self.assertTrue(type(a), Base)
#         self.assertIsInstance(a, Base)

#         # base has a method to_json_string(list_dictionaries)
#         # to_json_string devuelve un string

#         rect = Rectangle(10, 7, 2, 8)
#         dictionary = rect.to_dictionary()
#         json_dictionary = Base.to_json_string([dictionary])

#         self.assertTrue(type(dictionary) == dict)
#         self.assertTrue(type(json_dictionary) == str)

#         # base has a class method save_to_file
#         # writes the JSON string representation of a list of objs to a file

#         r1 = Rectangle(10, 7, 2, 8)
#         r2 = Rectangle(2, 4)
#         Rectangle.save_to_file([r1, r2])

#         with open("Rectangle.json", "r") as file:
#             readed = file.read()

#         self.assertTrue(len(readed) > 0)

#         s1 = Square(1, 7, 2)
#         s2 = Square(2, 4)
#         Square.save_to_file([s1, s2])

#         with open("Square.json", "r") as file:
#             readed = file.read()

#         self.assertTrue(len(readed) > 0)

#         os.remove("Rectangle.json")

#         Rectangle.save_to_file(None)

#         with open("Rectangle.json", "r") as file:
#             readed = file.read()

#         self.assertTrue(readed == '[]')

#         os.remove("Rectangle.json")
#         os.remove("Square.json")

#         # base has a static method from_json_string(json_string)
#         # from_json_string devuelve una lista

#         list_input = [
#             {'id': 89, 'width': 10, 'height': 4},
#             {'id': 7, 'width': 1, 'height': 7}
#         ]
#         json_list_input = Rectangle.to_json_string(list_input)
#         list_output = Rectangle.from_json_string(json_list_input)

#         self.assertTrue(type(list_input) == list)
#         self.assertTrue(type(json_list_input) == str)
#         self.assertTrue(type(list_output) == list)

#         list_output = Rectangle.from_json_string(None)

#         self.assertTrue(type(list_input) == list)
#         self.assertTrue(type(json_list_input) == str)
#         self.assertTrue(type(list_output) == list)
#         self.assertTrue(list_output == [])

#         # base has a class method create(cls, **dictionary)
#         # returns an object with all the attributes setted

#         r1 = Rectangle(3, 5, 1)
#         r1_dictionary = r1.to_dictionary()
#         r2 = Rectangle.create(**r1_dictionary)
#         self.assertTrue(r1.x == r2.x)
#         self.assertTrue(r1.y == r2.y)
#         self.assertTrue(r1.id == r2.id)
#         self.assertTrue(r1.width == r2.width)
#         self.assertTrue(r1.height == r2.height)
#         self.assertFalse(r1 is r2)
#         self.assertFalse(r1 == r2)

# if __name__ == '__main__':
#     unittest.main()
