#!/usr/bin/python3
<<<<<<< HEAD
""" State Module for the HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """class for amenities"""
    __tablename__ = 'amenities'
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity",
                                       back_populates="amenities")
    else:
        name = ""
=======
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Table, String, ForeignKey
from sqlalchemy.orm import relationship

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Amenity(BaseModel, Base):
    """ Reprrsents amenities for the database """
    __tablename__ = "amenities"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary=place_amenity)
    else:
        name = ""
>>>>>>> e60ed55b4b5c778952ea3e45151a3b87845b1743
