#!/usr/bin/python3
"""Script that defines all common
attributes/methods for other classes
"""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """the BaseModel to HBnB clone"""
    def __init__(self, *args, **kwargs):
        """Initializes instance attributes
        Args:
            - *args: arguments
            - **kwargs: key-values arguments
        """
        if kwargs:
            del kwargs["__class__"]
            for keys, value in kwargs.items():
                if keys == "updated_at" or keys == "created_at":
                    
                    dt_time = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, keys, dt_time)
                else:
                    setattr(self, keys, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """method that updates the instance updated_at"""

        self.updated_at = datetime.now()
        models.storage.save()
        
    def __str__(self):
        """Returns the String Representation
        within the model
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__
            )

    def to_dict(self):
        """return key values"""
        my_dict = {}
        my_dict["__class__"] = self.__class__.__name__
        
        for key, value in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                my_dict[key] = value.isoformat()
            else:
                my_dict[key] = value
        return dict(my_dict)
