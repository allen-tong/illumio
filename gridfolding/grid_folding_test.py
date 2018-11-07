#!/usr/bin/env python

import unittest

from grid_folding import Grid, GridError

class TestGridFolding(unittest.TestCase):

    def test_init(self):
        g = Grid(4)
        self.assertEqual(g.grid, [
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]
            ]
        ])

    def test_2_fold_top_to_bottom(self):
        g = Grid(2)
        g.fold_top_to_bottom()
        self.assertEqual(g.grid, [[[1, 2]], [[3, 4]]])

    def test_2_fold_bottom_to_top(self):
        g = Grid(2)
        g.fold_bottom_to_top()
        self.assertEqual(g.grid, [[[3, 4]], [[1, 2]]])

    def test_2_fold_right_to_left(self):
        g = Grid(2)
        g.fold_right_to_left()
        self.assertEqual(g.grid, [[[2], [4]], [[1], [3]]])

    def test_2_fold_left_to_right(self):
        g = Grid(2)
        g.fold_left_to_right()
        self.assertEqual(g.grid, [[[1], [3]], [[2], [4]]])

    def test_2_fold_vertical_then_horizontal(self):
        g = Grid(2)
        g.fold("TL")
        self.assertEqual(g.grid, [[[3]], [[1]], [[2]], [[4]]])

    def test_2_fold_horizontal_then_vertical(self):
        g = Grid(2)
        g.fold("RB")
        self.assertEqual(g.grid, [[[3]], [[4]], [[2]], [[1]]])

    def test_flatten(self):
        g = Grid(1)
        g.grid = [
            [[1]], [[2]], [[3]], [[4]], [[5]], [[6]], [[7]], [[8]],
            [[9]], [[10]], [[11]], [[12]], [[13]], [[14]], [[15]], [[16]]
        ]
        array = g.flatten()
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.assertEqual(array, expected)

    def test_4_all_folds_clockwise(self):
        g = Grid(4)
        array = g.fold("TRBL")
        expected = [9, 5, 8, 12, 16, 4, 1, 13, 14, 2, 3, 15, 11, 7, 6, 10]
        self.assertEqual(array, expected)

    def test_4_all_folds_vertical_then_horizontal(self):
        g = Grid(4)
        array = g.fold("TBLR")
        expected = [12, 8, 4, 16, 13, 1, 5, 9, 10, 6, 2, 14, 15, 3, 7, 11]
        self.assertEqual(array, expected)

    def test_4_all_folds_horizontal_then_vertical(self):
        g = Grid(4)
        array = g.fold("RLBT")
        expected = [2, 3, 4, 1, 13, 16, 15, 14, 10, 11, 12, 9, 5, 8, 7, 6]
        self.assertEqual(array, expected)

    def test_4_two_folds_grouped(self):
        g = Grid(4)
        array = g.fold("RRTT")
        expected = [9, 12, 11, 10, 6, 7, 8, 5, 1, 4, 3, 2, 14, 15, 16, 13]
        self.assertEqual(array, expected)

    def test_4_two_folds_interleaved(self):
        g = Grid(4)
        array = g.fold("BLBL")
        expected = [3, 15, 14, 2, 6, 10, 11, 7, 8, 12, 9, 5, 1, 13, 16, 4]
        self.assertEqual(array, expected)

    def test_16_too_many_vertical_folds(self):
        g = Grid(16)
        g.fold_bottom_to_top()
        g.fold_bottom_to_top()
        g.fold_top_to_bottom()
        g.fold_top_to_bottom()
        with self.assertRaisesRegex(GridError, "Too many vertical folds!"):
            g.fold_top_to_bottom()

    def test_16_too_many_horizontal_folds(self):
        g = Grid(16)
        g.fold_right_to_left()
        g.fold_left_to_right()
        g.fold_right_to_left()
        g.fold_left_to_right()
        with self.assertRaisesRegex(GridError, "Too many horizontal folds!"):
            g.fold_right_to_left()

    def test_short_input(self):
        g = Grid(16)
        with self.assertRaisesRegex(GridError,
                                    "Invalid input: incorrect input length"):
            g.fold("TBRLTRB")

    def test_long_input(self):
        g = Grid(16)
        with self.assertRaisesRegex(GridError,
                                    "Invalid input: incorrect input length"):
            g.fold("BTLRBLTRB")

    def test_invalid_character(self):
        g = Grid(16)
        with self.assertRaisesRegex(GridError, "Invalid input character: X"):
            g.fold("TBRLXBRL")

if __name__ == "__main__":
    unittest.main()
