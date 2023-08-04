#!/usr/bin/python3
"""This module contains tests for console"""

import unittest
from console import HBNBCommand


class testConsole(unittest.TestCase):
    """Defines the tests"""

    def test_consoleHas(self):
        """Tests for methods"""
        self.assertTrue(hasattr(HBNBCommand, "emptyline"))
        self.assertTrue(hasattr(HBNBCommand, "do_quit"))
        self.assertTrue(hasattr(HBNBCommand, "do_EOF"))
        self.assertTrue(hasattr(HBNBCommand, "do_create"))
        self.assertTrue(hasattr(HBNBCommand, "do_show"))
        self.assertTrue(hasattr(HBNBCommand, "do_destroy"))
        self.assertTrue(hasattr(HBNBCommand, "do_all"))
        self.assertTrue(hasattr(HBNBCommand, "do_update"))
        self.assertTrue(hasattr(HBNBCommand, "default"))


if __name__ == "__main__":
    unittest.main()
