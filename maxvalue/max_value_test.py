#!/usr/bin/env python

import unittest

from max_value import Street

class TestMaxValue(unittest.TestCase):

    def test_init(self):
        s = Street([6, "1", 2.5, "7.5"])
        self.assertEqual(s.houses, [6, 1, 2.5, 7.5])

    def test_basic(self):
        s = Street([6, 1, 2, 7])
        self.assertEqual(s.max_loot(), 13)

    def test_empty(self):
        s = Street([])
        self.assertEqual(s.max_loot(), 0)

    def test_one_house(self):
        s = Street([1])
        self.assertEqual(s.max_loot(), 1)

    def test_two_houses(self):
        s = Street([3, 7])
        self.assertEqual(s.max_loot(), 7)

    def test_three_houses_pick_one(self):
        s = Street([3, 10, 5])
        self.assertEqual(s.max_loot(), 10)

    def test_three_houses_pick_two(self):
        s = Street([3, 7, 5])
        self.assertEqual(s.max_loot(), 8)

    def test_adjacent_high_values(self):
        s = Street([3, 7, 20, 21, 5, 2])
        self.assertEqual(s.max_loot(), 28)

    def test_duplicates(self):
        s = Street([7, 3, 7, 5])
        self.assertEqual(s.max_loot(), 14)

    def test_long_s(self):
        s = Street([i * 77 % 100 for i in range(100)])
        self.assertEqual(s.max_loot(), 197)

    def test_floats(self):
        s = Street([3, 7.5, 5.5, 2])
        self.assertEqual(s.max_loot(), 9.5)

    def test_negative(self):
        with self.assertRaisesRegex(ValueError,
                                    "Input contains negative value: -7"):
            s = Street([3, -7, 5, 2])

    def test_invalid_value(self):
        with self.assertRaisesRegex(ValueError, "Invalid input value: hello"):
            s = Street([3, 7, "hello", 5, 2])

    def test_invalid_type(self):
        with self.assertRaisesRegex(TypeError, "Invalid input value: \[10\]"):
            s = Street([3, 7, [10], 5, 2])

if __name__ == "__main__":
    unittest.main()
