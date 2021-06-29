#!/usr/bin/python3
"""Defines State Class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class  saves the attributes of a state:
        - name (string)
    """
    name = ""
