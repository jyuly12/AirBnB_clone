#!/usr/bin/python3
"""This file defines the FileStorage class"""
import json
import os
# files used in eval() function
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage():
    """Serializes instances to a JSON file and deserializes JSON file
    to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key"""
        key_name = obj.__class__.__name__ + '.' + obj.id
        self.__objects.update({key_name: obj})

    def save(self):
        """Serializes __objects to the JSON file"""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as jsonfile:
            json.dump(my_dict, jsonfile)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, encoding='utf-8') as json_file:
                json_string = json_file.read()
            dict_of_objects = json.loads(json_string)
            for key in dict_of_objects:
                characteristics = dict_of_objects.get(key)
                # obtain the dictionary
                obtain_object = characteristics.get('__class__')
                new_object = eval(obtain_object)(**characteristics)
                # create object
                self.new(new_object)
                # save the object in the object dictionary
