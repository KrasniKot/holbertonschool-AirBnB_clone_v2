#!/usr/bin/python3
"""This module contains unittests for City"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """Defines the tests"""

    def __init__(self, *args, **kwargs):
        """Initializes a test"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Tests the attribute state_id"""
        new = self.value()
        self.assertTrue(hasattr(new, "state_id"))

    def test_name(self):
        """Tests the attribute name"""
        new = self.value()
        self.assertTrue(hasattr(new, "name"))


if __name__ == "__main__":
    unittest.main()
