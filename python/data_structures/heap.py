# -*- coding: utf-8 -*-

"""
    Binary Heap (Priority Queue)
    ----------------------------

    Define a generic binary heap (Heap) with a user-supplied compare function.
    The priority of an item can be updated.

    Also define MinHeap and MaxHeap as an example.

    Time Complexity of Operations:
        - Construct Heap from list : Θ( n )
        - Insert                   : O( logn )
        - Find First Item          : O( 1 )
        - Find & Remove First Item : O( logn )
        - Update Priority          : O( logn )
"""

class Heap:
    def __init__(self, cmpFn, elems=None):
        """
        cmpFn: A user-supplied compare function for the binary heap.
        elems: A list of initial elements with their priorities.
               Each element must be in the form (Item, Priority).
        """
        self.cmpFn = cmpFn
        self.A = [42]  # The element at position 0 is trash.
        self.n = 0
        self.pos = {}
        if elems != None:
            self.construct_heap(elems)

    def construct_heap(self, elems):
        """
        Construct a heap from a list of elements with priorities.
        Each element of the list must be in the form (Item, Priority).
        """
        for e in elems:
            self.n += 1
            self.A.append(e)
            self.pos[e[0]] = self.n
        for i in range(self.n // 2, 0, -1):
            self.combine(i)

    def get_first(self):
        """
        Gets the first item of the heap (but doesn't remove it).
        """
        return self.A[1][0] if self.n > 0 else None

    def delete_first(self):
        """
        Gets the first item of the heap and removes it.
        """
        if self.n == 0:
            return None
        first = self.A[1]
        self.n -= 1
        last = self.A.pop()
        if self.n > 0:
            self.A[1] = last
            self.combine(1)
        return first[0]

    def combine(self, i):
        l = 2*i
        r = l+1
        mp = i
        if (l <= self.n) and self.cmpFn(self.A[l][1], self.A[mp][1]):
            mp = l
        if (r <= self.n) and self.cmpFn(self.A[r][1], self.A[mp][1]):
            mp = r
        if mp != i:
            Ai, Amp = self.A[i], self.A[mp]
            self.pos[Ai[0]], self.pos[Amp[0]] = self.pos[Amp[0]], self.pos[Ai[0]] 
            self.A[i], self.A[mp] = Amp, Ai
            self.combine(mp)

    def insert(self, elem, prio):
        """
        Inserts the element elem with priority prio.
        """
        self.n += 1
        self.A.append( (e,w) )
        self.pos[e] = self.n
        i = self.n
        p = i // 2
        self.insert_loop(i, p)

    def insert_loop(self, i, p):
        while i > 1 and not self.cmpFn(self.A[p][1], self.A[i][1]):
            Ap, Ai = self.A[p], self.A[i]
            self.pos[Ai[0]], self.pos[Ap[0]] = self.pos[Ap[0]], self.pos[Ai[0]] 
            self.A[p], self.A[i] = Ai, Ap
            i = p
            p = i // 2

    def change_priority(self, elem, prio):
        """
        Changes the priority of the element elem to prio.
        """
        pos = self.pos[elem]
        currPrio = self.A[pos][1]
        self.A[pos] = (elem, prio)
        if self.cmpFn(prio, currPrio):
            self.insert_loop(pos, pos // 2)  # Up heapify
        else:
            self.combine(pos)  # Down heapify


class MinHeap(Heap):
    """
    A min heap.
    """
    def __init__(self, elems=None):
        Heap.__init__(self, lambda x,y: x < y, elems)

    def min(self):
        """
        Gets the minimum element of the heap.
        """
        return self.get_first()

    def take_min(self):
        """
        Gets the minimum element of the heap and removes it.
        """
        return self.get_first()

    def take_min(self):
        return self.delete_first()


class MaxHeap(Heap):
    """
    A max heap.
    """
    def __init__(self, elems=None):
        Heap.__init__(self, lambda x,y: x > y, elems)

    def max(self):
        """
        Gets the maximum element of the heap. 
        """
        return self.get_first()

    def take_max(self):
        """
        Gets the maximum element of the heap and removes it.
        """
        return self.delete_first()


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(999999999)
    # Simple MinHeap test (1).
    h = MinHeap()
    items = [('a',3), ('b',4), ('c',7), ('d',9), ('e',6), ('f',8), ('g',5), ('h',1)]
    for (e, w) in items:
        h.insert(e, w)
    xs = []
    while h.min():
        xs.append(h.take_min())
    assert xs == list(map(lambda x: x[0], sorted(items, key=lambda x: x[1])))
    # Simple MinHeap test (2).
    items = [('a',3), ('b',4), ('c',7), ('d',9), ('e',6), ('f',8), ('g',5), ('h',1)]
    h = MinHeap(items)
    xs = []
    while h.min():
        xs.append(h.take_min())
    assert xs == list(map(lambda x: x[0], sorted(items, key=lambda x: x[1])))
    # Change priorities in MinHeap.
    h = MinHeap()
    for (e, w) in items:
        h.insert(e, w)
    xs = [h.take_min(), h.take_min()]
    h.change_priority('c', 10)
    h.change_priority('f', 7)
    while h.min():
        xs.append(h.take_min())
    items[2] = ('c', 10)
    items[5] = ('f', 7)
    assert xs == list(map(lambda x: x[0], sorted(items, key=lambda x: x[1])))
    # Simple MaxHeap test.
    h = MaxHeap()
    items = [('a',3), ('b',4), ('c',7), ('d',9), ('e',6), ('f',8), ('g',5), ('h',1)]
    for (e, w) in items:
        h.insert(e, w)
    xs = []
    while h.max():
        xs.append(h.take_max())
    assert xs == list(map(lambda x: x[0], sorted(items, key=lambda x: x[1], reverse=True)))

