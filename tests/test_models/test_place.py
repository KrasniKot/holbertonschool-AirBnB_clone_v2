#!/usr/bin/python3
"""This module contains unittests for Place"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Defines the tests"""

    def __init__(self, *args, **kwargs):
        """Initializes a test"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Tests the attribute city_id"""
        new = self.value()
        self.assertTrue(hasattr(new, "city_id"))

    def test_user_id(self):
        """Test the attribute user_id"""
        new = self.value()
        self.assertTrue(hasattr(new, "user_id"))

    def test_name(self):
        """Tests the attribute name"""
        new = self.value()
        self.assertTrue(hasattr(new, "name"))

    def test_description(self):
        """Tests the attribute description"""
        new = self.value()
        self.assertTrue(hasattr(new, "description"))

    def test_number_rooms(self):
        """new has number_rooms"""
        new = self.value()
        self.assertTrue(hasattr(new, "number_rooms"))

    def test_number_bathrooms(self):
        """New has number_bathrooms"""
        new = self.value()
        self.assertTrue(hasattr(new, "number_bathrooms"))

    def test_max_guest(self):
        """new has max_guest"""
        new = self.value()
        self.assertTrue(hasattr(new, "max_guest"))

    def test_price_by_night(self):
        """new has price_by_night"""
        new = self.value()
        self.assertTrue(hasattr(new, "price_by_night"))

    def test_latitude(self):
        """new has latitude"""
        new = self.value()
        self.assertTrue(hasattr(new, "latitude"))

    def test_longitude(self):
        """new hast longitude"""
        new = self.value()
        self.assertTrue(hasattr(new, "longitude"))

    def test_amenity_ids(self):
        """new hast amenity_ids"""
        new = self.value()
        self.assertTrue(hasattr(new, "amenity_ids"))


if __name__ == "__main__":
    unittest.main()
