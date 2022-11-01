#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import models
from datetime import datetime
<<<<<<< HEAD
import sys
=======
>>>>>>> e60ed55b4b5c778952ea3e45151a3b87845b1743
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
<<<<<<< HEAD
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        if not kwargs:
            from models import storage
            
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if kwargs.get("created_at"):
                kwargs["created_at"] = datetime.strptime(
                    kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.created_at = datetime.now()
            if kwargs.get("updated_at"):
                kwargs["updated_at"] = datetime.strptime(
                    kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.updated_at = datetime.now()
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)
=======
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiation of a base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
                if 'id' not in kwargs:
                    self.id = str(uuid.uuid4())
                if 'created_at' not in kwargs:
                    self.created_at = datetime.now()
                if 'created_at' in kwargs and 'updated_at' not in kwargs:
                    self.updated_at = self.created_at
                else:
                    self.updated_at = datetime.now()

        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
>>>>>>> e60ed55b4b5c778952ea3e45151a3b87845b1743

    def __str__(self):
        """Returns a string representation of the instance"""
        return '[{}] ({}) {}'.format(
                type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """return a string rep"""
        return self.__str__()

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
<<<<<<< HEAD
        storage.new(self)
        storage.save()
=======
        models.storage.new(self)
        models.storage.save()
>>>>>>> e60ed55b4b5c778952ea3e45151a3b87845b1743

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__': (str(type(self))
                                         .split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
<<<<<<< HEAD
        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']
        
        return dictionary


    def delete(self):
        """delete the current instance from storage"""
        from models import storage
        storage.delete(self)
=======
        dictionary.pop("_sa_instance_state", None)

        return dictionary

    def delete(self):
        """deletes the current instance from storage"""
        models.storage.delete(self)
>>>>>>> e60ed55b4b5c778952ea3e45151a3b87845b1743
