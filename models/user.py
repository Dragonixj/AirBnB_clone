#!/usr/bin/python3
"""User class, subclass of parent BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class for storing user info"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
