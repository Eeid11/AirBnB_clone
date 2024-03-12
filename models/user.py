#!/usr/bin/python3
"""
This file inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """class"""
    # User 

    # class attributes
    email = ""
    password = ""
    first_name = ""
    last_name = ""
