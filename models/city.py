#!/usr/bin/python3
"""Impliment the City subclass."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city.

    Attributes:
        state_id (str): Id of state.
        name (str): name_of_city.
    """

    state_id = ""
    name = ""
