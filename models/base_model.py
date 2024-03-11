#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
import models


class base_model_11:

    def __init__(self, *args, **kwargs):

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
        format = "[{}] ({}) {}"
        return format.format(
                type(self).__name__,
                self.id,
                self.__dict__)

    def save(self):
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        temp = {**self.__dict__}
        temp['__class__'] = type(self).__name__
        temp['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        temp['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return temp

    @classmethod
    def all(cls):
        return models.storage.find_all(cls.__name__)

    @classmethod
    def counter(cls):
        return len(models.storage.find_all(cls.__name__))

    @classmethod
    def creation(cls, *args, **kwargs):
        new = cls(*args, **kwargs)
        return new.id

    @classmethod
    def show(cls, instance_id):
        """Retrieve an instance"""
        return models.storage.find_by_id(
            cls.__name__,
            instance_id
        )

    @classmethod
    def destroying(cls, instance_id):
        return models.storage.delete_by_id(
            cls.__name__,
            instance_id
        )

    @classmethod
    def updating(cls, instance_id, *args):
        if not len(args):
            print("** attribute name missing **")
            return
        if len(args) == 1 and isinstance(args[0], dict):
            args = args[0].items()
        else:
            args = [args[:2]]
        for arg in args:
            models.storage.update_one(
                cls.__name__,
                instance_id,
                *arg
            )
