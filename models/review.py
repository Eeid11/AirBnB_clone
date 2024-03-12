#!/usr/bin/python3
"""
Defines review model and inherits
from BaseModel
"""


from models.base_model import base_model


class Review(base_model):
    """class"""

    place_id = ''
    user_id = ''
    text = ''
