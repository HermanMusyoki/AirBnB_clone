#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represention of the city.

    Attributes:
        state_id (str): The state id.
        name (str): The city name
    """

    state_id = ""
    name = ""
