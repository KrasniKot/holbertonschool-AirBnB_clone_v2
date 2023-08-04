#!/usr/bin/python3
"""Contains tests for DBStorage"""

import pep8
import unittest
from models.engine.db_storage import DBStorage
from os import getenv


class TestDBStorage(unittest.TestCase):
    """Defines the tests for DBStorage"""

    def test_pep8(self):
        """Tests pycodestyle style"""
        style = pep8.StyleGuide(quiet=True)
        checking = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(checking.total_errors, 0, "fix pep8")

    @unittest.skipIf(getenv == ("HBNB_TYPE_STORAGE") == "file", "Won't pass")
    def test_ItHasAttr(self):
        """Tests for the attributes"""
        self.assertTrue(hasattr(DBStorage, "_DBStorage__engine"))
        self.assertTrue(hasattr(DBStorage, "_DBStorage__session"))
        self.assertTrue(hasattr(DBStorage, "all"))
        self.assertTrue(hasattr(DBStorage, "new"))
        self.assertTrue(hasattr(DBStorage, "save"))
        self.assertTrue(hasattr(DBStorage, "delete"))
        self.assertTrue(hasattr(DBStorage, "reload"))

    def test_type(self):
        """Tests for the type"""
        new = DBStorage()
        self.assertTrue(issubclass(new.__class__, DBStorage), True)


if __name__ == "__main__":
    unittest.main()
