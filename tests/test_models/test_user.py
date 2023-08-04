#!/usr/bin/python3
"""Contains tests for User"""

import pep8
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """Defines the tests"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Firstname"
        cls.user.last_name = "Lastname"
        cls.user.email = "anEmail@gmamil.com"
        cls.user.password = "aPasSWorD"

    def test_pep8(self):
        """Tests pycodestyle style"""
        style = pep8.StyleGuide(quiet=True)
        checking = style.check_files(['models/user.py'])
        self.assertEqual(checking.total_errors, 0, "fix pep8")

    def test_atributtes(self):
        """First name tests"""
        new = User()
        self.assertTrue(hasattr(new, 'email'))
        self.assertTrue(hasattr(new, 'id'))
        self.assertTrue(hasattr(new, 'created_at'))
        self.assertTrue(hasattr(new, 'updated_at'))
        self.assertTrue(hasattr(new, 'password'))
        self.assertTrue(hasattr(new, 'first_name'))
        self.assertTrue(hasattr(new, 'last_name'))

    def test_UserTypes(self):
        """tests attribute type for User"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.first_name), str)

    def test_type(self):
        """Tests for the type"""
        self.assertTrue(issubclass(self.user.__class__, User), True)


if __name__ == "__main__":
    unittest.main()
