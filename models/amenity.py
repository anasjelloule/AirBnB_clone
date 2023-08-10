#!/usr/bin/python3
"""Impliment the Amenity subclass."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.

    Attributes:
        name (str): name_of_amenity.
    """

    name = ""
