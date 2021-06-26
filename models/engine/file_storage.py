#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel #noborrar, se usan implicitamt en eval
from models.user import User #noborrar, se usan implicitamt en eval



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
        self.__objects.update({key_name: obj})

    def save(self):
        """Serializes __objects to the JSON file
        """
        my_dict = {}
        if len(self.__objects) >= 1:     
            for key, value in self.__objects.items():
                my_dict[key] = value.to_dict()
            string_representation = json.dumps(my_dict)
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
                characteristics = dict_of_objects.get(key) # obtener el diccionario
                new_object = eval(characteristics.get('__class__'))(**characteristics) # crear el objeto
                self.new(new_object) # guardar el objeto en el diccionario de objetos