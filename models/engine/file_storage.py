#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            same_type = dict()

            for key, obj in FileStorage.__objects.items():
                if obj.__class__ == cls:
                    same_type[key] = obj

            return same_type

        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        temp = {}
        for key, value in FileStorage.__objects.items():
            temp[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(FileStorage.__file_path, 'r', encoding="UTF-8") as f:
                temp = json.load(f)
                for key, value in temp.items():
                    FileStorage.__objects[key] = eval(value[
                                                    '__class__'])(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """deletes obj from __objects if it's inside"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)

            if FileStorage.__objects[key]:
                del FileStorage.__objects[key]
                self.save()

    def close(self):
        """Deserializes the json file to objects"""
        self.reload()
