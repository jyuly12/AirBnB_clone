#!/usr/bin/python3
"""Defines City Class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class saves  the attributes of a city:
        - state_id (string)
        - name (string)
    """
    state_id = ""
    name = ""
