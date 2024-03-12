#!/usr/bin/python3
"""Module for BaseModel"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """class"""

    all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """class"""
        """Constructor method for BaseModel class"""
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k,
                            datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                elif k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """class"""
        """String representation of BaseModel class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """class"""
        """Method to update the public instance
        attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """class"""
        """Method to return a dictionary containing
        all keys/values of __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
