#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represention of the place.

    Attributes:
        city_id (str): The id of the city
        user_id (str): The id of the user
        name (str): The place name
        description (str): The place description
        number_rooms (int): The rooms number of the place.
        number_bathrooms (int): The number of bathrooms
        max_guest (int): The maximum number of guests
        price_by_night (int): The price by night
        latitude (float): The latitude of the place location
        longitude (float): The longitude of the place location
        amenity_ids (list): A list of ids of the amenity
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
