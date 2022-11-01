#!/usr/bin/python3
<<<<<<< HEAD
"""This module defines a class to manage db storage for hbnb clone"""
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import models
=======
"""This module defines the DBStorage engine"""
from os import getenv
>>>>>>> e60ed55b4b5c778952ea3e45151a3b87845b1743
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
<<<<<<< HEAD


class DBStorage:
    """SQL database storage"""
=======
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """Class for DBStorage engine"""

>>>>>>> e60ed55b4b5c778952ea3e45151a3b87845b1743
    __engine = None
    __session = None

    def __init__(self):
<<<<<<< HEAD
        """Create engine and connect to database"""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        envv = getenv("HBNB_ENV", "none")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)

        if envv == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            lista = [State, City, User, Place, Review, Amenity]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return (dic)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
=======
        """Initialisation of DBStorage engine"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on current database session"""
        new_dict = {}
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if isinstance(cls, str):
                cls = eval(cls)
            objs = self.__session.query(cls)
            for o in objs:
                key = o.__class__.__name__ + '.' + o.id
                new_dict[key] = o
        return (new_dict)

    def new(self, obj):
        """adds obj to current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit new changes to current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes obj from current database session"""
>>>>>>> e60ed55b4b5c778952ea3e45151a3b87845b1743
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
<<<<<<< HEAD
        """Create current database session from the engine
        using a sessionmaker"""
        self.__session = Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()

    def close(self):
        """Remove session"""
=======
        """creates all tables in database and creates new session"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session()

    def close(self):
        """to close current database session"""
>>>>>>> e60ed55b4b5c778952ea3e45151a3b87845b1743
        self.__session.close()
