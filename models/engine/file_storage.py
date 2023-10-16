#!/usr/bin/python3
"""
Contains the FileStorage class model
"""
import json
import os

from models.user import User
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.base_model import BaseModel


class FileStorage:
    """
    serializes instances to a JSON file
    and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file(path: __file_path)"""
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            d_storage = {}
            for key, value in self.__objects.items():
                d_storage[key] = value.to_dict()
            json.dump(d_storage, f)

    def classes(self):
        """returns a dictionary of valid classes and their references"""

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }
        return classes

    def reload(self):
        """deserializes the JSON file to __objects(only if the JSON file(
        __file_path)exists)"""
        if not os.path.isfile(self.__file_path):
            return
        with open(self.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {
                k: self.classes()[v["__class__"]](**v) for k, v in obj_dict.items()
            }
            self.__objects = obj_dict
