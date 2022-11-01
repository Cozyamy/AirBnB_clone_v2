#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
<<<<<<< HEAD
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel, Base):
    """ Review class to store review information """
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
=======
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
>>>>>>> e60ed55b4b5c778952ea3e45151a3b87845b1743
