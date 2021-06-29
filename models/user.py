#!/usr/bin/python3
"""Defines user module"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class attributes:
        - email (string)
        - password (string)
        - first_name (string)
        - last_name (string)
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
