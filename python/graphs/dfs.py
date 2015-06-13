# -*- coding: utf-8 -*-

"""
    DFS Algorithm
    -------------

    Graph Representation: Adjacency list

    Parameters:
    Graph
        The graph is a dict, where each vertex maps to a dict of its neighbours.
        The neighbour list is a dict that maps neighbour vertices to the weight
        of the edge.
    Root
        The root vertex.

    Returns:
    The tuple (Parent, Cost) where
    Parent
        A dict that maps each vertex to its parent node, so as to reconstruct
        the tree, if necessary.
    Cost
        A dict that maps each vertex to the cost of the path that starts at
        the root at ends at the vertex. If the vertex is not reachable, then
        the cost is infinite.
"""

import collections

def dfs(graph, root):
    pending = collections.deque([root])
    parent = {root: None}
    visited = set() 
    inf = float("inf")
    cost = collections.defaultdict(lambda: inf)
    cost[root] = 0

    while len(pending):
        u = pending.pop()
        if u not in visited: 
            visited.add(u)
            for (v, w) in graph[u].items():
                if v not in visited:
                    parent[v] = u
                    cost[v] = cost[u] + w
                    pending.append(v)

    return parent, cost

if __name__=="__main__":
    graph = dict()
    graph[0] = {1: 1, 3: 1, 4: 1, 5: 1, 6: 1}
    graph[1] = {2: 1, 4: 1}
    graph[2] = {}
    graph[3] = {5: 1}
    graph[4] = {6: 1}
    graph[5] = {2: 1}
    graph[6] = {3: 1}
    parent, cost = dfs(graph, 0)
    assert cost[2] == 4
    assert parent[2] == 5
    assert parent[5] == 3
    assert parent[3] == 6
    assert parent[6] == 0
