#!/usr/bin/python3
"""Script defines all common attributes/methods for other classes"""

import uuid
from datetime import datetime

class BaseModel:
    """the BaseModel to HBnB clone"""

    def save(self):
        """method that updates the instance updated_at"""

        self.updated_at = datetime.now()
        
    def __str__(self):
        """Returns the String Representation
        within the model
        """
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
    
    