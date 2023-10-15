#!/usr/bin/python3
"""Defines unittests for models/base_model.py"""
import unittest
import os
from datetime import datetime
import models
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test suite for the models.base_model.BaseModel
    """

    def test_str_representation(self):
        """
        Checks if the string representation is correct
        """
        bm = BaseModel()
        self.assertEqual(str(bm), "[BaseModel] ({}) {}".format(bm.id, bm.__dict__))

    def test_if_BaseModel_instance_has_id(self):
        """Checks if id is assigned to instance during initialization"""
        bm = BaseModel()
        self.assertTrue(hasattr(bm, "id"))

    def test_if_id_is_unique(self):
        """
        Checks if id is generated uniquely
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_id_type_is_str(self):
        """
        Checks that id is a str object
        """
        bm = BaseModel()
        self.assertTrue(str, type(bm.id))

    def test_created_at_is_datetime(self):
        """
        Checks that attribute 'created_at' is a datetime object
        """
        bm = BaseModel()
        self.assertTrue(datetime, type(bm.created_at))

    def test_updated_at_is_datetime(self):
        """
        Checks that attribute 'updated_at' is a datetime object
        """
        bm = BaseModel()
        self.assertTrue(datetime, type(bm.updated_at))
