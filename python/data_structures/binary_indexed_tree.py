# -*- coding: utf-8 -*-

"""
    Binary Indexed Tree
    -------------------

    Based on the proposed C/C++ implementation by
    Yannis Chatzimichos @ https://git.softlab.ntua.gr/public/pdp-camp/blob/master/2013/advanced_data_structures.pdf

    Supports the operations
    - ADD S X
        Add X to the sum at position S
    - SUM X Y
        Finds the sum from position X to position Y

    The binary indexed tree is 1-indexed.

    Time Complexity
        All the operations cost O( logn ), where n is the number of bits of the position.
"""

class BIT:
    def __init__(self, n):
        self.bit = (n + 1) * [0]  # Position 0 is not used.
        self.n = n

    def add(self, pos, x):
        while pos <= self.n:
            self.bit[pos] += x
            pos += (pos & -pos)

    def sum(self, x, y):
        sy = self.sumFromOne(y)
        return sy if x == 1 else sy - self.sumFromOne(x)

    def sumFromOne(self, pos):
        sum = 0
        while pos > 0:
            sum += self.bit[pos]
            pos -= (pos & -pos)
        return sum

if __name__ == "__main__":
    xs = [7,0,3,2,3,0,0,4,6,3,2,8]
    n = len(xs)
    bit = BIT(n)
    for i in range(1, n+1):
        bit.add(i, xs[i-1])
    assert ([bit.sum(1, x) for x in range(1, n+1)]) == [sum(xs[0:n]) for n in range(1, n+1)]
    bit.add(5, 3)
    assert bit.sum(2, n) == sum(xs[2:]) + 3
