# -*- coding: utf-8 -*-

"""
    Segment Tree
    ------------

    Based on the proposed C/C++ implementation by
    Yannis Chatzimichos @ https://git.softlab.ntua.gr/public/pdp-camp/blob/master/2013/advanced_data_structures.pdf

    This implementation assumes ranges from 1 to n, where points are integers.
    If a range from x to y is required, it must be first be mapped to the range from 1 to (y-x).

    The constructor requires:
    N
        The 1..N range.
    Comp
        The comparator function.

    Supports the operations:
    UPDATE X V
        Updates the value at position X to V.
    QUERY X Y
        Queries the range from position X to Y.

    Time Complexity
        All the operations cost O( logn ), where n is the length of the whole range.
"""

class SegmentTree:
    def __init__(self, n, comp):
        self.comp = comp
        self.segs = (3 * n + 1) * [0]  # Position 0 is not used.
        self.n = n
    
    def update(self, pos, val):
        self.update0(pos, val, 1, self.n, 1)

    def update0(self, pos, val, x, y, id):
        if x == y:
            self.segs[id] = val
            return
        mid = (x + y) // 2
        left = 2 * id
        right = left + 1
        if pos <= mid:
            self.update0(pos, val, x, mid, left)
        else:
            self.update0(pos, val, mid + 1, y, right)
        self.segs[id] = self.comp(self.segs[left], self.segs[right])

    def query(self, x, y):
        return self.query0(x, y, 1, self.n, 1)

    def query0(self, qx, qy, x, y, id):
        if x == qx and y == qy:
            return self.segs[id]
        mid = (x + y) // 2
        mid1 = mid + 1
        left = 2 * id
        right = left + 1
        if qy <= mid:
            return self.query0(qx, qy, x, mid, left)
        elif qx > mid:
            return self.query0(qx, qy, mid1, y, right)
        else:
            return self.comp(self.query0(qx, mid, x, mid, left),
                             self.query0(mid1, qy, mid1, y, right))


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(999999999)
    sg = SegmentTree(10, lambda x,y: max(x,y))
    sg.update(9, 5)
    sg.update(6, 3)
    assert sg.query(1, 10) == 5
    assert sg.query(6, 8) == 3
    assert sg.query(7, 9) == 5
    assert sg.query(3, 9) == 5
    assert sg.query(2, 7) == 3
