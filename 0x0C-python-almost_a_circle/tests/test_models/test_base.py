#!/usr/bin/python3
""" Base unittest"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base1 = Base()
        cls.base2 = Base()
        cls.base3 = Base()
        cls.base4 = Base(20)

    def test_id(self):
        self.assertEqual(self.base1.id, 1)
        self.assertEqual(self.base2.id, 2)
        self.assertEqual(self.base3.id, 3)

    def test_id_parameter(self):
        self.assertEqual(self.base4.id, 20)

    def test_increment(self):
        Base.__nb_objects = 0

        self.assertEqual(self.base1.id, 1)


if __name__ == "__main__":
    unittest.main()
