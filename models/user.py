#!/usr/bin/python3
"""User class, subclass of parent BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class for storing user info
    Attributes:
        email(str) - user's email
        password(str) - user's password
        first_name(str) - User's first first name
        last_name(str) - user's last name"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
