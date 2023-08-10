#!/usr/bin/python3
"""Impliment the Review subclass."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a classreview.

    Attributes:
        place_id (str): id_of_Place.
        user_id (str): id_of_User.
        text (str): text_of_review.
    """

    place_id = ""
    user_id = ""
    text = ""
