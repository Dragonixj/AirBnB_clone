#!/usr/bin/python3
"""contains the subclass Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """implements the review model"""

    place_id = ""
    user_id = ""
    text = ""
