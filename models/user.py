#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
<<<<<<< HEAD
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """ This class defines a user by various attributes """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
=======
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place", backref="user", cascade="delete")
        reviews = relationship("Review", backref="user", cascade="delete")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
>>>>>>> e60ed55b4b5c778952ea3e45151a3b87845b1743
