#!/usr/bin/python3
"""contains unittests for HBNBCommand"""

import unittest


class test_HBNBCommand(unittest.TestCase):
    """Defines tests for HBNBComand"""

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
