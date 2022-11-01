#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
<<<<<<< HEAD
        """Returns a dictionary of models currently in the storage"""
        if not cls:
            return FileStorage.__objects
        else:
            newdict = {}
            for key, value in self.__objects.items():
                if type(value) == cls:
                    newdict[key] = value
            return newdict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Saves storage dictionary to file"""
        temp = {}
        temp.update(FileStorage.__objects)
        for key, val in temp.items():
            temp[key] = val.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(FileStorage.__file_path, "r", encoding="UTF8") as fd:
                for val in json.load(fd).values():
                    class_name = val["__class__"]
                    del val["__class__"]
                    self.new(eval(class_name)(**val))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects"""
        if obj:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Deserializing the JSON file to objects"""
=======
        """Returns all the objects"""
        if cls:
            same_type = dict()

            for key, obj in self.__objects.items():
                if obj.__class__ == cls:
                    same_type[key] = obj

            return same_type

        return self.__objects

    def new(self, obj):
        """sets __object to given obj"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path"""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                json_dict = json.load(f)
                for value in json_dict.values():
                    cls = value['__class__']
                    self.new(eval('{}({})'.format(cls, '**value')))
        except (FileNotFoundError):
            pass

    def delete(self, obj=None):
        """Delete obj from __objects if it's inside"""
        if obj is not None:
            try:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                if self.__objects[key]:
                    del self.__objects[key]
                self.save()
            except (KeyError):
                pass

    def close(self):
        """Deserialize the JSON file to objects"""
>>>>>>> e60ed55b4b5c778952ea3e45151a3b87845b1743
        self.reload()
