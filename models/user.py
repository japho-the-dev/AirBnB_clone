#!/usr/bin/python3
"""Model that creates a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class contining user constants"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""