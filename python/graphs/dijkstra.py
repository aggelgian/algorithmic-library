# -*- coding: utf-8 -*-

"""
    Dijkstra's ALgorithm
    --------------------

    Finds the shortest paths between nodes in a graph

    Parameters:
    Graph
        The graph as an adjacency list.
    Root
        The root vertex.

    Returns:
    Cost
        A dictionary that maps vertices to the cost of the shortest path from the root to them.
    Parent
        A dictionary tham maps vertices to their parent in the shortest path from the root to them.
        It is needed to reconstruct the shortest path.

    Complexity
        Θ( |E| log(|V|) ) -- Using a Binary Heap
"""

import collections
from heap import MinHeap

def dijkstra(graph, root):
    vertices = graph.keys()
    n = len(vertices)

    # Initialize the priority queue
    inf = float("inf")
    pq = MinHeap([(v, inf) for v in graph.keys()]) 
    pq.change_priority(root, 0)
    # Other initializations
    parent = collections.defaultdict(lambda: None)
    selected = set()
    cost = collections.defaultdict(lambda: inf)
    cost[root] = 0

    while len(selected) < n:
        u = pq.min()
        du = cost[u] = pq.get_priority(u)
        selected.add(u)
        pq.take_min()
        for (v, w) in graph[u].items():
            if v not in selected and pq.get_priority(v) > du + w:
                pq.change_priority(v, du + w)
                parent[v] = u
    
    return cost, parent


if __name__ == "__main__":
    graph = dict()
    graph[1] = {2: 7, 3: 9, 6: 14}
    graph[2] = {1: 7, 3: 10, 4: 15}
    graph[3] = {1: 9, 2: 10, 4: 11, 6: 2}
    graph[4] = {2: 15, 3: 11, 5: 6}
    graph[5] = {4: 6, 6: 9}
    graph[6] = {1: 14, 3: 2, 5: 9}
    cost, parent = dijkstra(graph, 1)
    assert cost == collections.defaultdict(lambda: inf, {1: 0, 2: 7, 3: 9, 4: 20, 5: 20, 6: 11})
    assert parent == collections.defaultdict(lambda: None, {2: 1, 3: 1, 4: 3, 5: 6, 6: 3})
