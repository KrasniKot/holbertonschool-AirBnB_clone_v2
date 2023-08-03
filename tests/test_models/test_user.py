#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def test_first_name(self):
        """ """
        new = User()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = User()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = User()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = User()
        self.assertEqual(type(new.password), str)
