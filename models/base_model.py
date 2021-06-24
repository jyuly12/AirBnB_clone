#!/usr/bin/python3
"""Defines BaseModel class
"""
import uuid


class BaseModel:
    """Defines all common attributes/methods for other classes
    """
    def __init__(self):
        """Initialize the instance attributes
        """
        self.id = uuid.uuid4

    def __str__(self):

    def save(self):

    def to_dict(self):
