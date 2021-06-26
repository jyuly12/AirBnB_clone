#!/usr/bin/python3
"""Defines Amenity Class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class saves the attibutes of an amenity:
        - name (string)
    """
    name = ""