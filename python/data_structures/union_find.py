# -*- coding: utf-8 -*-

"""
    Union-Find Data Structure
    -------------------------

    Description from
        - https://en.wikipedia.org/wiki/Disjoint-set_data_structure
        - http://www.algorithmist.com/index.php/Union_Find

    Union-Find is a data structure that keeps track of a set of elements partitioned
    into a number of disjoint (nonoverlapping) subsets.

    Using the optimizations:
        - Union by rank
        - Path compression
    The amortized running time per operation is O( a(n) ), where a denotes the inverse of the Ackermann function.

    Construction:
        Nodes
            The list of elements that constitute the initial disjoint sets.
"""

class UnionFind:
    def __init__(self, nodes):
        """
        Creates disjoints sets for all the nodes.
        The rank of all the nodes is 0.
        """
        self.ancestors = {}
        for node in nodes:
            self.ancestors[node] = (node, 1, 0)

    def __str__(self):
        parts = []
        for node in self.ancestors:
            (parent, n, rnk) = self.ancestors[node]
            parts.append("[%s] Parent: %s, N: %d, Rank: %d" % (node, parent, n, rnk))
        return "\n".join(parts)

    def find(self, node):
        """
        Finds the representative of the set that node belongs to.
        """
        visited = []  # Will store the nodes in the path to the root
        while True:
            (parent, n, rnk) = self.ancestors[node]
            if node == parent:
                # Set the parent of the encountered nodes to the root (path compression)
                for (node1, n1, rnk1) in visited:
                    self.ancestors[node1] = (node, n1, rnk1)
                return node
            else:
                visited.append( (node, n, rnk) )
                node = parent

    def union(self, node1, node2):
        """
        Joins the two subsets, that node1 and node2 belong to, into a single subset.
        """
        # Find the representatives of each subset.
        rep1 = self.find(node1)
        rep2 = self.find(node2)
        if rep1 == rep2:
            return
        (_, n1, rnk1) = self.ancestors[rep1]
        (_, n2, rnk2) = self.ancestors[rep2]
        # Apply union by rank.
        # If they have the same rank, then choose a random parent and increase its rank.
        if rnk1 == rnk2:
            self.ancestors[rep2] = (rep1, n2, rnk2)
            self.ancestors[rep1] = (rep1, n1 + n2, rnk1 + 1)
        # Else the node with the higher rank becomes the parent.
        elif rnk1 > rnk2:
            self.ancestors[rep2] = (rep1, n2, rnk2)
            self.ancestors[rep1] = (rep1, n1 + n2, rnk1)
        else:
            self.ancestors[rep2] = (rep2, n1 + n2, rnk2)
            self.ancestors[rep1] = (rep2, n1, rnk1)

    def nodes_in_set(self, node):
        """
        Returns the cardinality of the subset that node belongs to.
        """
        (_, n, _) = self.ancestors[node]
        return n

if __name__ == "__main__":
    import random
    nodes = list("abcdefghijklmnopqrstuvwxyz")
    uf = UnionFind(nodes)
    for _ in range(1000):
        x = random.choice(nodes)
        y = random.choice(nodes)
        uf.union(x, y)
    root = uf.find(random.choice(nodes))
    assert uf.nodes_in_set(root) == 26
