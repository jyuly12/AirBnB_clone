#!/usr/bin/python3
"""Defines Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class  saves the attributes of an place:
        - city_id (string)
        - user_id string)
        - name (string)
        - description (string)
        - number_rooms (integer)
        - number_bathrooms (integer)
        - max_guest (integer)
        - price_by_night (integer)
        - latitude (float)
        - longitude (float)
        - amenity_ids (list of strings)
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
