#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represention of the state.

    Attributes:
        name (str): The state name
    """

    name = ""
