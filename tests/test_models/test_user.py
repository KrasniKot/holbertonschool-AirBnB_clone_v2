#!/usr/bin/python3
"""Contains tests for User"""
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


if __name__ == "__main__":
    unittest.main()
