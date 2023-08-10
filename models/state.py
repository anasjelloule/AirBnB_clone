#!/usr/bin/python3
"""Impliment the State subclass."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a class state.

    Attributes:
        name (str): name_of_state.
    """

    name = ""
