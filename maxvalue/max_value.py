#!/usr/bin/env python

import sys

class Street:
    """Representation of a line of houses.

    Each house is represented by a nonnegative numeric value
    corresponding to how much a thief could potentially steal
    from that house.
    """

    def __init__(self, houses):
        self.houses = []
        for elem in houses:
            try:
                val = float(elem)
            except (TypeError, ValueError) as e:
                e.args = ("Invalid input value: {}".format(elem),)
                raise
            if val < 0:
                raise ValueError("Input contains negative value: {}"
                                 .format(val))
            self.houses.append(float(val))

    def max_loot(self):
        """Return the maximum value that can be stolen from this street."""
        if not self.houses:
            return 0
        if len(self.houses) == 1:
            return self.houses[0]
        max_left = self.houses.copy()
        max_right = self.houses.copy()
        for i in range(1, len(self.houses)):
            max_left[i] = max(max_left[i - 1], self.houses[i])
            max_right[-(i + 1)] = max(max_right[-i], self.houses[-(i + 1)])
        max_values = []
        max_values.append(max_right[1])
        for i in range(1, len(self.houses) - 1):
            max_values.append(max_left[i - 1] + max_right[i + 1])
        max_values.append(max_left[-2])
        return max(max_values)

    def max_loot_alternate(self):
        """Return the maximum value that can be stolen from this street.

        Returns the same value as max_loot(); however, requires fewer
        passes over the input array and can be modified to run with
        constant space.
        """
        if not self.houses:
            return 0
        if len(self.houses) == 1:
            return self.houses[0]
        max_val = max(self.houses)
        max_index = self.houses.index(max_val)
        max_removed = self.houses[: max(0, max_index - 1)] \
                      + self.houses[max_index + 2 :]
        if len(max_removed) > 0:
            max_val += max(max_removed)
        if max_index == 0 or max_index == len(self.houses) - 1:
            return max_val
        else:
            return max(max_val,
                       self.houses[max_index - 1] + self.houses[max_index + 1])

if __name__ == "__main__":
    try:
        street = Street(sys.argv[1:])
        print(street.max_loot())
    except (TypeError, ValueError) as e:
        print(e)
