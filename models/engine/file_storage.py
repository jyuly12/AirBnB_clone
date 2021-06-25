#!/usr/bin/python3
import json
import os


class FileStorage():
    """Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key
        """
        key_name = obj.__class__.__name__ + '.' + obj.id
        self.__objects: obj.to_dict()
        print("objects=", self.__objects)

    def save(self):
        """Serializes __objects to the JSON file
        """
        print("__objects=", self.__objects)
        if len(self.__objects) >= 1:                     
            string_representation = json.dumps(self.__objects)
            with open (self.__file_path, 'w', encoding='utf-8') as jsonfile:
                jsonfile.write(string_representation)
        
    def reload(self):
        """Deserializes the JSON file to __objects
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, encoding='utf-8') as jsonfile:
                jsonstring = jsonfile.read()
            dict_of_objects = json.loads(jsonstring)
            for key in dict_of_objects:
                from models.base_model import BaseModel
                characteristics = dict_of_objects.get(key)
                new_object = BaseModel(**characteristics)
                self.new(new_object)
