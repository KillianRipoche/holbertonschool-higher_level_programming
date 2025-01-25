#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([1, 2]), 2)

    def test_negative(self):
        self.assertEqual(max_integer([-5, -700]), -5)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_long_list(self):
        self.assertEqual(max_integer([5, 6, 9, -5, 1000, 123, 59]), 1000)

    def test_strings(self):
        self.assertEqual(max_integer(["5", "6", "9", "-5"]), "9")

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_only_one(self):
        self.assertEqual(max_integer([77]), 77)
if __name__ == "__main__":
    unittest.main()
