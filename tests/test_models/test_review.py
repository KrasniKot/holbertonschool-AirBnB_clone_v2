#!/usr/bin/python3
"""Contains tests for Review"""

import pep8
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Defines the tests"""

    def __init__(self, *args, **kwargs):
        """Initializes a test"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review
        self.rev = Review()
        self.rev.place_id = "40285"
        self.rev.user_id = "032"
        self.rev.text = "The Text"

    def test_pep8(self):
        """Tests pycodestyle style"""
        style = pep8.StyleGuide(quiet=True)
        checking = style.check_files(['models/review.py'])
        self.assertEqual(checking.total_errors, 0, "fix pep8")

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

    def test_ReviewTypesAttr(self):
        """tests attribute type for Review"""
        self.assertEqual(type(self.rev.text), str)
        self.assertEqual(type(self.rev.place_id), str)
        self.assertEqual(type(self.rev.user_id), str)

    def test_type(self):
        """Tests for the type"""
        new = Review()
        self.assertTrue(issubclass(new.__class__, Review), True)


if __name__ == "__main__":
    unittest.main()
