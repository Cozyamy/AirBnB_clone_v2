#!/usr/bin/python3
<<<<<<< HEAD
'''The Package initializer'''
=======
"""This module instantiates an object of class FileStorage"""
>>>>>>> e60ed55b4b5c778952ea3e45151a3b87845b1743
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

<<<<<<< HEAD
storage.reload()
=======
if getenv('HBNB_TYPE_STORAGE') == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
>>>>>>> e60ed55b4b5c778952ea3e45151a3b87845b1743
