#!/usr/bin/python3
"""
Contains the FileStorage class model
"""
import json


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

    def reload(self):
        """deserializes the JSON file to __objects(only if the JSON file(
        __file_path)exists)"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj = json.load(f)
                for object in obj.values():
                    name = object["__class__"]
                    del object["__class__"]
                    self.new(eval(name)(**object))
        except FileNotFoundError:
            return
