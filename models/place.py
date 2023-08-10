#!/usr/bin/python3
"""Impliment the Place subclass."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place class.

    Attributes:
        city_id (str): Id_of_City.
        user_id (str): Id_of_User.
        name (str): name_of_place.
        description (str): description_of_place.
        number_rooms (int): number_of_rooms_of_place.
        number_bathrooms (int): number_of_bathrooms_of_place.
        max_guest (int): maximum number_of_guests_of_place.
        price_by_night (int): price by night_of_place.
        latitude (float): latitude_of_place.
        longitude (float): longitude_of_place.
        amenity_ids (list): list_of_Amenity ids.
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
