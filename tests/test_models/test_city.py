#!/usr/bin/python3
"""This module contains unittests for City"""

import pep8
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """Defines the tests"""

    def __init__(self, *args, **kwargs):
        """Initializes a test"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City
        self.city = City()
        self.city.name = "disffds"
        self.city.state_id = "asdfklj"

    def test_pep8(self):
        """Tests pycodestyle style"""
        style = pep8.StyleGuide(quiet=True)
        checking = style.check_files(['models/city.py'])
        self.assertEqual(checking.total_errors, 0, "fix pep8")

    def test_state_id(self):
        """Tests the attribute state_id"""
        new = self.value()
        self.assertTrue(hasattr(new, "state_id"))

    def test_name(self):
        """Tests the attribute name"""
        new = self.value()
        self.assertTrue(hasattr(new, "name"))

    def test_CityTypes(self):
        """Tests attribute type for City"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_type(self):
        """Tests for the type"""
        new = City()
        self.assertTrue(issubclass(new.__class__, City), True)


if __name__ == "__main__":
    unittest.main()
