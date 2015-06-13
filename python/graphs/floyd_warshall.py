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

    Time Complexity:
        Θ( n^3 )
"""

import collections

def floyd_warshall(graph):
    vertices = graph.keys()
    n = len(vertices)

    # Initialize the cost matrix.
    inf = float("inf")
    cost = dict()
    cost[0] = dict()
    for u in vertices:
        cost[0][u] = collections.defaultdict(lambda: inf)
        neighbours = graph[u]
        for v in vertices:
            if v in neighbours:
                cost[0][u][v] = neighbours[v]
        cost[0][u][u] = 0

    # Run the algorithm.
    for k in range(1, n + 1):
        cost[k] = dict()
        for i in range(1, n + 1):
            cost[k][i] = collections.defaultdict(lambda: inf)
            for j in range(1, n + 1):
                cost[k][i][j] = min( cost[k-1][i][j],
                                     cost[k-1][i][k] + cost[k-1][k][j] )

    return cost[n]


if __name__ == "__main__":
    inf = float("inf")
    graph = dict()
    graph[1] = {2: 1, 4: -2}
    graph[2] = {3: -1, 4: 3}
    graph[3] = {4: 2}
    graph[4] = {5: 4}
    graph[5] = {1: 3, 2: 5}
    cost = floyd_warshall(graph)
    assert cost[1] == collections.defaultdict(lambda: inf, {1: 0, 2: 1, 3: 0, 4: -2, 5: 2})
    assert cost[2] == collections.defaultdict(lambda: inf, {1: 8, 2: 0, 3: -1, 4: 1, 5: 5})
    assert cost[3] == collections.defaultdict(lambda: inf, {1: 9, 2: 10, 3: 0, 4: 2, 5: 6})
    assert cost[4] == collections.defaultdict(lambda: inf, {1: 7, 2: 8, 3: 7, 4: 0, 5: 4})
    assert cost[5] == collections.defaultdict(lambda: inf, {1: 3, 2: 4, 3: 3, 4: 1, 5: 0})
