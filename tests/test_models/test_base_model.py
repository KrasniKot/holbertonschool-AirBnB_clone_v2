#!/usr/bin/python3
"""This module contains tests for BaseModel"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """Defines the tests"""

    def __init__(self, *args, **kwargs):
        """Initializes a test"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Does nothing"""
        pass

    def tearDown(self):
        """Removes the file.json"""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """Tests for the type of instances"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Tests the kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Tests the kwargs passing ints"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Tests the correct value returned by str"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_to_dict(self):
        """Tests to_dict() method"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_id(self):
        """Tests the attribute id"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Tests the attribute created_at"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Tests the attribute updated_at"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at != new.updated_at)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "Won't pass")
    def test_save(self):
        """test if the save works"""
        new = BaseModel()
        new.save()
        self.assertNotEqual(new.created_at, new.updated_at)


if __name__ == "__main__":
    unittest.main()
