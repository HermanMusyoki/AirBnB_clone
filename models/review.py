#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represention of the review.

    Attributes:
        place_id (str): The id of the place
        user_id (str): The id of the user
        text (str): The review text
    """

    place_id = ""
    user_id = ""
    text = ""
