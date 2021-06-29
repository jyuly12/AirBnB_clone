#!/usr/bin/python3
"""Defines BaseModel class
"""
import uuid
from datetime import datetime


class BaseModel():
    """Defines all common  attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """Initialize the instance attributes
        Class Attributes:
        - id (string)
        - created_at (datetime)
        - updated_at (datetime)
        """
        if kwargs:
            for i in kwargs.keys():
                if i != "__class__":
                    setattr(self, i, kwargs.get(i))
                if i == 'created_at' or i == 'updated_at':
                    value = datetime.strptime(kwargs.get(i),
                                              "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, i, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models.__init__ import storage
            storage.new(self)

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                      self.__dict__))

    def save(self):
        """Updates the public instance attribute"""
        self.updated_at = datetime.now()
        from models.__init__ import storage
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of
        the instance
        """
        dictionary = self.__dict__.copy()
        dictionary.update({"__class__": self.__class__.__name__})
        dictionary.update({"created_at": self.created_at.isoformat()})
        dictionary.update({"updated_at": self.updated_at.isoformat()})
        return dictionary
