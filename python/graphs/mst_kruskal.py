# -*- coding: utf-8 -*-

"""
    Kruskal's MST Algorithm
    ---------------------

    Offers two functions that calculate the Minimum Spanning Tree of an undirected graph.

    - kruskal
        Parameters:
            Edges
                A list of the graph's edges.
                Each element is a tuple in the form ((From, To), Weight).
            Vertices
                A list of the graph's vertices.
        

    - kruskal_from_graph
        Parameters:
            Graph
                The graph as an adjacency list.
        
    Both return the tuple (Cost, Mst) where
        Cost
            The weight of the MST.
        Mst
            The edges selected in the MST.
            Each edge is in the form (From, To).

    Complexity
        Θ( |E| log(|E|) )
"""

from union_find import UnionFind

def kruskal_from_graph(graph):
    """
    Runs the Kruskal algorithm using the graph representation.
    """
    # Create the list of edges.
    edges = dict() 
    for u in graph:
        neighbours = graph[u]
        for v in neighbours:
            edges[( min(u,v), max(u,v) )] = neighbours[v]

    return kruskal(edges.items(), graph.keys())


def kruskal(edges, vertices):
    """
    Runs the Kruskal algorithm using the edges and vertices.
    """
    cost = 0
    mst = []
    n = len(vertices)

    # Sort the edges by weight.
    edges = sorted(edges, key=lambda x: x[1])
    uf = UnionFind(vertices)

    for ((u, v), w) in edges:
        # If the edge doesn't create a circle
        if uf.find(u) != uf.find(v):
            # add it to the MST.
            uf.union(u, v)
            mst.append( (u,v) )
            cost += w
            # Stop when the MST has |V|-1 edges.
            if len(mst) == n-1:
                return cost, mst
    

if __name__ == "__main__":
    # Graph representation
    graph = dict()
    graph[1] = {2: 1, 3: 2,}
    graph[2] = {1: 1, 3: 3, 4: 5}
    graph[3] = {1: 2, 2: 3, 4: 4}
    graph[4] = {2: 5, 3: 4}
    (cost, mst) = kruskal_from_graph(graph)
    assert cost == 7
    assert sorted(mst) == [(1,2), (1,3), (3,4)]
    # Edges & vertices already calculated
    edges = [((1,2), 1), ((2,3), 3), ((3,4), 4), ((2,4), 5), ((1,3), 2)]
    vertices = [1, 2, 3, 4]
    (cost, mst) = kruskal(edges, vertices)
    assert cost == 7
    assert sorted(mst) == [(1,2), (1,3), (3,4)]
