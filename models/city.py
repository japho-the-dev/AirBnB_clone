#!/usr/bin/python3
"""Modelthat creates City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """class for managing city objects-
    state_id and name
    """
    state_id = ""
    name = ""