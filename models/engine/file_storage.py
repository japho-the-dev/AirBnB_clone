#!/usr/bin/python3
"""serializes instances to a JSON file 
and deserializes JSON file to instances
"""
import os.path
import json
import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Storage for Data and Retrieval"""
    __file_path = "file.json"
    __objects = {}

    def classes(self):
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
        with open(FileStorage.__file_path, "F", encoding="utf-8") as filename:
            x = {y: z.to_dict() for y, z in FileStorage.__objects.items()}
            json.dump(x, filename)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
    

