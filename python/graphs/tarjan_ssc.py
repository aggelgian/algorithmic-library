# -*- coding: utf-8 -*-

"""
    Tarjan's Strongly Connected Components Algorithm
    ================================================

    Parameters:
    Graph
        The graph as an adjacency list.

    Returns:
        SSC
           A list of all the strongly connected components. Each SSC is a list of
           the vertices it contains.

    Time Complexity:
        O( |V| + |E| )
"""

import collections

def tarjan_ssc(graph):
    idx = {"n" : 0}
    index = collections.defaultdict(lambda: None)
    lowlink = dict()
    onStack = set()
    stack = []
    ssc = []

    for u in graph.keys():
        if index[u] == None:
            strong_connect(u, graph, idx, index, lowlink, onStack, stack, ssc)
    
    return ssc

def strong_connect(u, graph, idx, index, lowlink, onStack, stack, ssc):
    index[u] = idx["n"]
    lowlink[u] = idx["n"]
    idx["n"] += 1
    stack.append(u)
    onStack.add(u)

    # Check the neighbours of u.
    for v in graph[u]:
        if index[v] == None:
            strong_connect(v, graph, idx, index, lowlink, onStack, stack, ssc)
            lowlink[u] = min(lowlink[u], lowlink[v])
        elif v in onStack:
            lowlink[u] = min(lowlink[u], lowlink[v])

    # If it's a root node then generate an SSC
    if lowlink[u] == index[u]:
        component = []
        while True:
            w = stack.pop()
            onStack.remove(w)
            component.append(w)
            if w == u:
                ssc.append(component)
                break



if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(999999999)
    graph = dict()
    graph[1] = {5: 1}
    graph[2] = {1: 1}
    graph[3] = {2: 1, 4: 1}
    graph[4] = {3: 1}
    graph[5] = {2: 1}
    graph[6] = {2: 1, 5: 1, 7: 1}
    graph[7] = {3: 1, 6: 1}
    graph[8] = {4: 1, 7: 1}
    ssc = tarjan_ssc(graph)
    sol = [[1, 2, 5], [3, 4], [6, 7,], [8]]
    assert sorted(sorted(x) for x in ssc) == sorted(sorted(x) for x in sol)
