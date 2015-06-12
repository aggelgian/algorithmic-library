# -*- coding: utf-8 -*-

"""
    Helper classes to map hashable objects to integers.

    IntMapper
        Helps to map a range of hashable objects to integers.

    GraphMapper
        Helps to create a graph of hashable objects to a graph of integers.
"""

class IntMapper:
    """
    The default behaviour is to add an item and get back an integer to represent it.
    In many cases the original object is not needed. However, if you need to retrieve the
    original item from its integer then the parameter with_lookup should be set to True.
    """
    
    def __init__(self, with_lookup=False, n=0):
        """
        with_lookup: Whether you want to be able to retrieve an item by its number.
        n: The first integer to map an item to.
        """
        self.table = dict() 
        self.index = n
        self.revTable = dict() if with_lookup else None

    def add(self, item):
        """
        Adds an item and returns its representing integer.
        """
        idx = self.index
        self.table[item] = idx
        if self.revTable != None:
            self.revTable[idx] = item
        self.index += 1
        return idx

    def lookup_index(self, idx):
        """
        Looks up an item by its representing integer.
        If you need this behaviour, set with_lookup to True when creating the mapper.
        """
        return self.revTable[idx] if self.revTable != None else None

    def lookup_item(self, item):
        """
        Looks up the representing integer of an item.
        """
        return self.table[item]



class GraphMapper:
    """
    The default behaviour is to add a vertex and get back an integer to represent it.
    In many cases the original vertex is not needed. However, if you need to retrieve the
    original vertex from its integer then the parameter with_lookup should be set to True.
    """
    def __init__(self, with_lookup=False):
        """
        with_lookup: Whether you want to be able to retrieve a vertex by its number.
        """
        self.graph = dict()
        self.mapper = IntMapper(with_lookup)

    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph and returns its representing integer.
        """
        idx = self.mapper.add(vertex)
        self.graph[idx] = dict()
        return idx
    
    def add_edge(self, vertex1, vertex2, w):
        """
        Adds an edge to the graph.
        """
        u = self.mapper.lookup_item(vertex1)
        v = self.mapper.lookup_item(vertex2)
        self.graph[u][v] = w
        
    def get_graph(self):
        """
        Gets the created graph
        """
        return self.graph

    def lookup_vertex(self, vertex):
        """
        Gets the representing integer of a vertex.
        """
        return self.mapper.lookup_item(vertex)

    def lookup_index(self, idx):
        """
        Looks up a vertex by its representing integer.
        If you need this behaviour, set with_lookup to True when creating the mapper.
        """
        return self.mapper.lookup_index(idx)


if __name__ == "__main__":
    items = ["a", "b", "c"]
    # Test IntMapper.
    imp = IntMapper(True)
    indexes = []
    for item in items:
        indexes.append(imp.add(item))
    for idx in indexes:
        item = items[idx]
        assert item == imp.lookup_index(idx)
        assert idx == imp.lookup_item(item)
    # Test GraphMapper.
    gmp = GraphMapper()
    indexes = []
    for item in items:
        indexes.append(gmp.add_vertex(item))
    gmp.add_edge(items[0], items[1], 1)
    graph = gmp.get_graph()
    assert graph[indexes[0]][indexes[1]] == 1
