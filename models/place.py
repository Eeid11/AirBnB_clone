#!/usr/bin/python3
"""
Defines the Place model,
that inherits from BaseModel
"""


from models.base_model import BaseModel
from typing import List


class Place(BaseModel):
    """class"""
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms:  int = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude:  float = 0.0
    amenity_ids:  List[str] = []
