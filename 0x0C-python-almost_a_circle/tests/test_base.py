#!/usr/bin/python3
""" Base unittest"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """class for base class"""

    @classmethod
    def setUpClass(cls):
        """test init class"""
        cls.base1 = Base()
        cls.base2 = Base()
        cls.base3 = Base()
        cls.base4 = Base(20)

    def test_id(self):
        """method that tests id"""
        self.assertEqual(self.base1.id, 1)
        self.assertEqual(self.base2.id, 2)
        self.assertEqual(self.base3.id, 3)

    def test_id_parameter(self):
        """method that tests id parameter"""
        self.assertEqual(self.base4.id, 20)

    def test_increment(self):
        """method that tests increment"""
        Base.__nb_objects = 0

        self.assertEqual(self.base1.id, 1)
