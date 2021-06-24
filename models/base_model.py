#!/usr/bin/python3
"""Defines BaseModel class
"""
import uuid
import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes
    """
    def __init__(self):
        """Initialize the instance attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__, self.id, self.__dict__))

    def save(self):
        """Updates the public instance attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        dictionary = self.__dict__
        dictionary.update({"__class__": self.__class__})
        dictionary.update({"created_at": self.created_at.isoformat()})
        dictionary.update({"updated_at": self.updated_at.isoformat()})
        return dictionary
