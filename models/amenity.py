#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represention of the amenity.

    Attributes:
        name (str): The amenity name
    """

    name = ""
