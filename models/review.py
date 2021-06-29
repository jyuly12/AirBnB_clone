#!/usr/bin/python3
"""Defines Review Class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class  saves the attributes of a review:
        - place_id (string)
        - user_id (string)
        - text (string)
    """
    place_id = ""
    user_id = ""
    text = ""
