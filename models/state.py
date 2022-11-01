#!/usr/bin/python3
""" State Module for HBNB project """
<<<<<<< HEAD
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models
=======
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
>>>>>>> e60ed55b4b5c778952ea3e45151a3b87845b1743


class State(BaseModel, Base):
    """ State class """
<<<<<<< HEAD
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          backref="state", cascade="all, delete,delete-orphan")

    if getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            """ returns list of City instances related to state """
            from models import storage
            list_cities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
=======
    __tablename__ = "states"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')
    else:
        name = ""

        @property
        def cities(self):
            cities = list()

            for _id, city in models.storage.all(City).items():
                if city.state_id == self.id:
                    cities.append(city)

            return cities
>>>>>>> e60ed55b4b5c778952ea3e45151a3b87845b1743
