# -*- coding: utf-8 -*-

"""
    Floyd - Warshall Algorithm
    --------------------------

    Finds the shortest paths from all the vertices in a weighted graph with positive or negative edge weights
    (but with no negative cycles).

    Parameters:
    Graph
        The graph as an adjacency list.

    Returns:
    Cost
        A dictionary where the element Cost[u][v] denotes the cost of the shortest path from u to v.
    Parent
        A dictionary where each row i is a dictionary that maps vertices to their parent in
        the shortest path from i to them.
        It is needed to reconstruct the shortest paths.

    Time Complexity:
        Θ( n^3 )
"""

import collections

def floyd_warshall(graph):
    vertices = graph.keys()
    n = len(vertices)

    # Initialize the cost & parent matrices.
    inf = float("inf")
    cost, parent = dict(), dict()
    for u in vertices:
        cost[u] = collections.defaultdict(lambda: inf)
        parent[u] = collections.defaultdict(lambda: None)
        neighbours = graph[u]
        for (v, w) in neighbours.items():
            cost[u][v] = w
            parent[u][v] = u
        cost[u][u] = 0

    # Run the algorithm.
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if cost[i][j] > cost[i][k] + cost[k][j]:
                    cost[i][j] = cost[i][k] + cost[k][j]
                    parent[i][j] = parent[k][j]

    return cost, parent


if __name__ == "__main__":
    inf = float("inf")
    graph = dict()
    graph[1] = {2: 1, 4: -2}
    graph[2] = {3: -1, 4: 3}
    graph[3] = {4: 2}
    graph[4] = {5: 4}
    graph[5] = {1: 3, 2: 5}
    cost, parent = floyd_warshall(graph)
    assert cost[1] == collections.defaultdict(lambda: inf, {1: 0, 2: 1, 3: 0, 4: -2, 5: 2})
    assert cost[2] == collections.defaultdict(lambda: inf, {1: 8, 2: 0, 3: -1, 4: 1, 5: 5})
    assert cost[3] == collections.defaultdict(lambda: inf, {1: 9, 2: 10, 3: 0, 4: 2, 5: 6})
    assert cost[4] == collections.defaultdict(lambda: inf, {1: 7, 2: 8, 3: 7, 4: 0, 5: 4})
    assert cost[5] == collections.defaultdict(lambda: inf, {1: 3, 2: 4, 3: 3, 4: 1, 5: 0})
    assert parent[1] == collections.defaultdict(lambda: None, {2: 1, 3: 2, 4: 1, 5: 4})
    assert parent[2] == collections.defaultdict(lambda: None, {1: 5, 3: 2, 4: 3, 5: 4})
    assert parent[3] == collections.defaultdict(lambda: None, {1: 5, 2: 1, 4: 3, 5: 4})
    assert parent[4] == collections.defaultdict(lambda: None, {1: 5, 2: 1, 3: 2, 5: 4})
    assert parent[5] == collections.defaultdict(lambda: None, {1: 5, 2: 1, 3: 2, 4: 1})
