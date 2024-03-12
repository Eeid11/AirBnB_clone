#!/usr/bin/python3
"""class"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """class"""
    def __init__(self, *args, **kwargs):
        """class"""

        if kwargs == {}:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
            return

        if 'id' not in kwargs:
            kwargs['id'] = str(uuid4())
        self.id = kwargs['id']

        for Key, val in kwargs.items():
            if Key == "__class_":
                continue
        if "created_at" in kwargs:
            self.created_at = datetime.strptime(
                    kwargs['created_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')
        if "updated_at" in kwargs:
            self.updated_at = datetime.strptime(
                    kwargs['updated_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        """class"""
        format = "[{}] ({}) {}"
        return format.format(
                type(self).__name__,
                self.id,
                self.__dict__)

    def save(self):
        """class"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """class"""
        temp = {**self.__dict__}
        temp['__class__'] = type(self).__name__
        temp['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        temp['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return temp

    @classmethod
    def all(cls):
        """class"""
        return models.storage.find_all(cls.__name__)
