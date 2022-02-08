#!/usr/bin/python3
"""Rectangle module test"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """class for rectangle test"""

    @classmethod
    def setUpClass(cls):
        """tests init class"""
        cls.rec1 = Rectangle(5, 4)
        cls.rec2 = Rectangle(5, 4, 7)
        cls.rec3 = Rectangle(5, 4, 8, 9)

    def test_width(self):
        """method that tests width"""
        self.assertEqual(self.rec1.width, 5)

    def test_height(self):
        """method that tests height"""
        self.assertEqual(self.rec1.height, 4)

    def test_x(self):
        """method that tests x"""
        self.assertEqual(self.rec2.x, 7)

    def test_y(self):
        """method that tests y"""
        self.assertEqual(self.rec3.y, 9)

    def test_negative_x(self):
        """method that tests negative x"""
        with self.assertRaises(ValueError) as cm:
            rectangle = Rectangle(6, 7, -9)

    def test_negative_y(self):
        """method that tests negative y"""
        with self.assertRaises(ValueError) as cm:
            rectangle = Rectangle(6, 7, 9, -9)

    def test_negative_width(self):
        """method that tests negative width"""
        with self.assertRaises(ValueError) as cm:
            rectangle = Rectangle(-4, 6)

    def test_negative_height(self):
        """method that tests negative height"""
        with self.assertRaises(ValueError) as cm:
            rectangle = Rectangle(4, -7)
