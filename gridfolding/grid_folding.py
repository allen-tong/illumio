#!/usr/bin/env python

import math
import sys

class Grid:
    """Representation of a sheet of grid paper.

    Initialized as a three-dimensional N x N x 1 grid.
    N must be a power of 2.
    Cells are numbered from 1 to N * N, going in order from
    left to right, then top to bottom, then front to back.
    """

    def __init__(self, N):
        try:
            if not float(N).is_integer():
                raise GridError("Grid length must be an integer")
            if N < 1 or (N & (N - 1) != 0):
                raise GridError("Grid length must be a power of 2")
        except (TypeError, ValueError):
            raise GridError("Invalid grid length: {}".format(N))
        self.grid = [[[N * i + j + 1 for j in range(N)] for i in range(N)]]
        self.max_folds = math.log(N, 2)
        self.vertical_folds = 0
        self.horizontal_folds = 0

    def fold_top_to_bottom(self):
        """Fold the top edge of the grid down to the bottom edge."""
        if self.vertical_folds >= self.max_folds:
            raise GridError("Too many vertical folds!")
        g = self.grid
        new_grid = []
        for i in reversed(range(len(g))):
            sheet = []
            for j in reversed(range(len(g[i]) // 2)):
                sheet.append(g[i][j])
            new_grid.append(sheet)
        for i in range(len(g)):
            sheet = []
            for j in range(len(g[i]) // 2, len(g[i])):
                sheet.append(g[i][j])
            new_grid.append(sheet)
        self.grid = new_grid
        self.vertical_folds += 1

    def fold_bottom_to_top(self):
        """Fold the top edge of the grid down to the bottom edge."""
        if self.vertical_folds >= self.max_folds:
            raise GridError("Too many vertical folds!")
        g = self.grid
        new_grid = []
        for i in reversed(range(len(g))):
            sheet = []
            for j in reversed(range(len(g[i]) // 2, len(g[i]))):
                sheet.append(g[i][j])
            new_grid.append(sheet)
        for i in range(len(g)):
            sheet = []
            for j in range(len(g[i]) // 2):
                sheet.append(g[i][j])
            new_grid.append(sheet)
        self.grid = new_grid
        self.vertical_folds += 1

    def fold_right_to_left(self):
        """Fold the top edge of the grid down to the bottom edge."""
        if self.horizontal_folds >= self.max_folds:
            raise GridError("Too many horizontal folds!")
        g = self.grid
        new_grid = []
        for i in reversed(range(len(g))):
            sheet = []
            for j in range(len(g[i])):
                sheet.append(g[i][j][: len(g[i][j]) // 2 - 1 : -1])
            new_grid.append(sheet)
        for i in range(len(g)):
            sheet = []
            for j in range(len(g[i])):
                sheet.append(g[i][j][: len(g[i][j]) // 2])
            new_grid.append(sheet)
        self.grid = new_grid
        self.horizontal_folds += 1

    def fold_left_to_right(self):
        """Fold the top edge of the grid down to the bottom edge."""
        if self.horizontal_folds >= self.max_folds:
            raise GridError("Too many horizontal folds!")
        g = self.grid
        new_grid = []
        for i in reversed(range(len(g))):
            sheet = []
            for j in range(len(g[i])):
                sheet.append(g[i][j][len(g[i][j]) // 2 - 1 : : -1])
            new_grid.append(sheet)
        for i in range(len(g)):
            sheet = []
            for j in range(len(g[i])):
                sheet.append(g[i][j][len(g[i][j]) // 2 :])
            new_grid.append(sheet)
        self.grid = new_grid
        self.horizontal_folds += 1

    def flatten(self):
        """Return the grid as a one-dimensional array.

        The grid must have dimensions 1 x 1 x N.
        """
        if (len(self.grid[0]) != 1) or (len(self.grid[0][0]) != 1):
            raise GridError("Cannot flatten grid until fully folded")
        return [sheet[0][0] for sheet in self.grid]

    def fold(self, sequence):
        """Fold the grid according to the given sequence.

        "T" folds the top edge of the grid down to the bottom edge.
        "B" folds the bottom edge of the grid up to the top edge.
        "R" folds the right edge of the grid across to the left edge.
        "L" folds the left edge of the grid across to the right edge.
        A valid sequence results in a 1 x 1 x N grid.
        """
        if len(sequence) != 2 * self.max_folds:
            raise GridError("Invalid input: incorrect input length")
        fold_funcs = {
            "T": self.fold_top_to_bottom,
            "B": self.fold_bottom_to_top,
            "R": self.fold_right_to_left,
            "L": self.fold_left_to_right
        }
        for c in sequence:
            f = fold_funcs.get(c)
            if not f:
                raise GridError("Invalid input character: {}".format(c))
            f()
        return self.flatten()

class GridError(Exception):
    pass

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: expected single sequence argument")
    else:
        try:
            g = Grid(16)
            print(g.fold(sys.argv[1]))
        except GridError as e:
            print(e)
