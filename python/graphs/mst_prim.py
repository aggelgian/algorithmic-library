# -*- coding: utf-8 -*-

"""
    Prim's MST ALgorithm
    --------------------

    Calculate the Minimum Spanning Tree of an undirected graph.

    Parameters:
    Graph
        The graph as an adjacency list.
    Root
        The root vertex.

    Returns sthe tuple (Cost, Mst) where
        Cost
            The weight of the MST.
        Mst
            The edges selected in the MST.
            Each edge is in the form (From, To).

    Complexity
        Θ( |E| log(|V|) ) -- Using a Binary Heap
"""

import collections
from heap import MinHeap

def prim(graph, root):
    vertices = graph.keys()
    n = len(vertices)

    # Initialize the priority queue
    inf = float("inf")
    pq = MinHeap([(v, inf) for v in graph.keys()]) 
    pq.change_priority(root, 0)
    # Other initializations
    parent = collections.defaultdict(lambda: None)
    selected = set()
    cost = 0
    mst = []

    while len(selected) < n:
        u = pq.take_min()
        selected.add(u)
        for (v, w) in graph[u].items():
            if not v in selected and w < pq.get_priority(v):
                pq.change_priority(v, w)
                parent[v] = u
        pu = parent[u]
        if pu != None:
            mst.append( (min(u,pu), max(u,pu)) )
            cost += graph[u][pu]
    
    return cost, mst


if __name__ == "__main__":
    graph = dict()
    graph[1] = {2: 1, 3: 2,}
    graph[2] = {1: 1, 3: 3, 4: 5}
    graph[3] = {1: 2, 2: 3, 4: 4}
    graph[4] = {2: 5, 3: 4}
    (cost, mst) = prim(graph, 1)
    assert cost == 7
    assert sorted(mst) == [(1,2), (1,3), (3,4)]
