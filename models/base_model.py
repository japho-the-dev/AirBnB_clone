#!/usr/bin/python3
"""Script that defines all common
attributes/methods for other classes
"""

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """the BaseModel to HBnB clone"""

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes
        Args:
            - *args: arguments
            - **kwargs: key-values arguments
        """
    if kwargs is not None and kwargs != {}:
        for key_value in kwargs:
            if key_value == "created_at":
                """Merges "created_at" to a datetime object"""
                self.__dict__["created_at"] = datetime.strptime(
                    kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            elif key_value == "updated_at":
                """Merges "updated_at" to a datetime object"""
                self.__dict__["updated_at"] = datetime.strptime(
                    kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                """If the key is neither "created_at" 
                nor "updated_at," set it as an attribute"""
                self.__dict__[key_value] = kwargs[key_value]
    else:
        """Generate a new UUID as a string"""
        self.id = str(uuid.uuid4()) 
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """method that updates the instance updated_at"""

        self.updated_at = datetime.now()
        
    def __str__(self):
        """Returns the String Representation
        within the model
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def to_dict(self):
        """return key values"""
        A_dict = self.__dict__.copy()
        A_dict["__class__"] = type(self).__name__
        A_dict["created_at"] = A_dict["created_at"].isoformat()
        A_dict["updated_at"] = A_dict["updated_at"].isoformat()
        return A_dict