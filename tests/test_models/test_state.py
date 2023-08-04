#!/usr/bin/python3
"""Contains tests for state"""

import pep8
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Defines the tests"""

    def __init__(self, *args, **kwargs):
        """Initializes a test"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_pep8(self):
        """Tests pycodestyle style"""
        style = pep8.StyleGuide(quiet=True)
        checking = style.check_files(['models/state.py'])
        self.assertEqual(checking.total_errors, 0, "fix pep8")

    def test_name3(self):
        """New has name"""
        new = self.value()
        self.assertTrue(hasattr(new, "name"))

    def test_type(self):
        """Tests for the type"""
        new = State()
        self.assertTrue(issubclass(new.__class__, State), True)


if __name__ == "__main__":
    unittest.main()
