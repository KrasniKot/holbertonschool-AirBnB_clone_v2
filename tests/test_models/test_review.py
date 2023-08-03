#!/usr/bin/python3
"""Contains tests for Review"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Defines the tests"""

    def __init__(self, *args, **kwargs):
        """Initializes a test"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Tests the attribute place_id"""
        new = self.value()
        self.assertTrue(hasattr(new, "place_id"))

    def test_user_id(self):
        """Tests the atributte user_id"""
        new = self.value()
        self.assertTrue(hasattr(new, "user_id"))

    def test_text(self):
        """Tests the atributte"""
        new = self.value()
        self.assertTrue(hasattr(new, "text"))


if __name__ == "__main__":
    unittest.main()
