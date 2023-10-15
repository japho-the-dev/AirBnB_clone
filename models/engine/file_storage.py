#!/usr/bin/python3
"""serializes instances to a JSON file 
and deserializes JSON file to instances
"""
import os
import json


class FileStorage:
    """Storage for Data and Retrieval"""
    __file_path = "file.json"
    __objects = {}

    def classes(self):

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review
        
        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def all(self):
        """Outputs the dict __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key_F = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key_F] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        my_dict = {}
        with open(FileStorage.__file_path, "w", encoding="utf8") as file:
            for key, value in FileStorage.__objects.items():
                my_dict[key] = value.to_dict()
            json.dump(my_dict, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for objs in data.values():
                    cls_key = objs["__class__"]
                    c_name = self.classes()[cls_key]
                    self.new(c_name(**objs))
        except FileNotFoundError:
            pass
