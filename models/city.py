#!/usr/bin/python3
"""City model."""

from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city."""

    state_id = ""
    name = ""