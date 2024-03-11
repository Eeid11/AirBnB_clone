#!/usr/bin/python3
"""
Defines review model and inherits
from BaseModel
"""


from models.base_model import base_model_11


class Review(base_model_11):
    # Review model

    # Attributes
    place_id: str = ''
    user_id: str = ''
    text: str = ''
