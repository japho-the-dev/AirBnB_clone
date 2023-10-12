#!/usr/bin/python3
"""Model to build Review class"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Class for review constants"""

    place_id = ""
    user_id = ""
    text = ""