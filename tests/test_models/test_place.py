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
        self.place = Place()
        self.place.city_id = "adfljk3"
        self.place.user_id = "453ui"
        self.place.name = "IDK"
        self.place.description = "IDK"
        self.place.number_rooms = 100394
        self.place.number_bathrooms = 9
        self.place.max_guest = 642
        self.place.price_by_night = 21
        self.place.latitude = 1.1
        self.place.longitude = 10.0
        self.place.amenity_ids = ["adfs8a7df"]

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

    def test_PlaceTypes(self):
        """Tests attribute type for Place"""
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    def test_type(self):
        """Tests for the type"""
        new = Place()
        self.assertTrue(issubclass(new.__class__, Place), True)


if __name__ == "__main__":
    unittest.main()
