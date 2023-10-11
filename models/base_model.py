#!/usr/bin/python3
"""
A module that implements the BaseModel class
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    A class that serves as a base for all common attributes and other classes
    """

    def __init__(self, *args, **kwargs):
        """Initializes the instance attributes"""
