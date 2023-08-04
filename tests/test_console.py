#!/usr/bin/python3
"""This module contains tests for console"""

import unittest
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Defines the tests"""

    def test_consoleAttrs(self):
        """Tests the attributes of console"""
        self.assertTrue(hasattr(HBNBCommand, "emptyline"))
        self.assertTrue(hasattr(HBNBCommand, "do_quit"))
        self.assertTrue(hasattr(HBNBCommand, "do_EOF"))
        self.assertTrue(hasattr(HBNBCommand, "do_create"))
        self.assertTrue(hasattr(HBNBCommand, "do_create"))
        self.assertTrue(hasattr(HBNBCommand, "do_destroy"))
        self.assertTrue(hasattr(HBNBCommand, "do_all"))
        self.assertTrue(hasattr(HBNBCommand, "do_update"))
        self.assertTrue(hasattr(HBNBCommand, "default"))
