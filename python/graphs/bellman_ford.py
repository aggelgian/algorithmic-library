# -*- coding: utf-8 -*-

"""
    Bellman - Ford Algorithm
    ------------------------

    Finds the shortest paths between nodes in a graph.
    The graph may have edges of negative weight.
    It requires the absence of negative-weight cycles.

    Parameters:
    Graph
        The graph as an adjacency list.
    Root
        The root vertex.

    Returns:
    Cost
        A dictionary that maps vertices to the cost of the shortest path from the root to them.
    Parent
        A dictionary that maps vertices to their parent in the shortest path from the root to them.
        It is needed to reconstruct the shortest path.

    If a cycle of negative weight is detected, then it returns the tuple (None, None)

    Complexity
        Θ( |E||V| )
"""

import collections

def bellman_ford(graph, root):
    inf = float("inf")
    cost = collections.defaultdict(lambda: inf)
    cost[root] = 0
    parent = collections.defaultdict(lambda: None)

    for _ in range(1, len(graph.keys())):
        for v in graph:
            neighbours = graph[v]
            for (u, w) in neighbours.items():
                if cost[u] > cost[v] + w:
                    cost[u] = cost[v] + w
                    parent[u] = v

    # Detect if there exists a negative-weight cycle.
    for v in graph:
        neighbours = graph[v]
        for (u, w) in neighbours.items():
            if cost[u] > cost[v] + w:
                return None, None

    return cost, parent


if __name__ == "__main__":
    inf = float("inf")
    graph = dict()
    graph['s'] = {'a': 6, 'b': 8}
    graph['a'] = {'c': -5, 'd': 4}
    graph['b'] = {'a': 7, 'c': 2}
    graph['c'] = {'d': -4, 'e': 3}
    graph['d'] = {'e': 2, 'f': 5}
    graph['e'] = {'b': 1, 'f': 2}
    graph['f'] = {}
    cost, parent = bellman_ford(graph, 's')
    assert cost == collections.defaultdict(lambda: inf, {'a': 6, 'b': 0, 'c': 1, 'd': -3, 'e': -1, 'f': 1, 's': 0})
    assert parent == collections.defaultdict(lambda: None, {'a': 's', 'b': 'e', 'c': 'a', 'd': 'c', 'e': 'd', 'f': 'e'})
