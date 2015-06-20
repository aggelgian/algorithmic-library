# -*- coding: utf-8 -*-

"""
    Trie
    ----

    Based on the proposed C/C++ implementation by
    Yannis Chatzimichos @ https://git.softlab.ntua.gr/public/pdp-camp/blob/master/2013/advanced_data_structures.pdf

    Supports
    - multiple insertions of the same word
    - count the words that have a specific prefix
    
    Time Complexity
        All the operations cost O( n ), where n is the length of the word
"""

class TrieNode:
    def __init__(self, letters, n):
        self.children = n * [None]
        self.wordCount = 0
        self.prefixes = 0
        self.idx = letters

    def setChild(self, letter, nextNode):
        self.children[self.idx[letter]] = nextNode

    def getChild(self, letter):
        return self.children[self.idx[letter]]

    def increaseWordCount(self):
        self.wordCount += 1

    def decreaseWordCount(self):
        self.wordCount -= 1

    def increasePrefixes(self):
        self.prefixes += 1

    def decreasePrefixes(self):
        self.prefixes -= 1

class Trie:
    def __init__(self, alphabet = "abcefghijklmnopqrstuvwxyz"):
        # Map the letters to list indices.
        self.letters = {}
        i = 0
        for l in alphabet:
            self.letters[l] = i
            i += 1
        self.n = len(alphabet)
        # Initialize the trie.
        self.nodes = [42, TrieNode(self.letters, self.n)]  # Node 0 is trash, Node 1 is the root
        self.trieNodeCount = 1

    def add(self, word):
        nextNode = currNode = 1
        for w in word:
            nextNode = self.nodes[currNode].getChild(w)
            if nextNode == None:
                self.trieNodeCount += 1
                self.nodes.append(TrieNode(self.letters, self.n))
                self.nodes[currNode].setChild(w, self.trieNodeCount)
                currNode = self.trieNodeCount
            else:
                currNode = nextNode
            self.nodes[currNode].increasePrefixes()
        self.nodes[currNode].increaseWordCount()

    def remove(self, word):
        currNode = 1
        for w in word:
            currNode = self.nodes[currNode].getChild(w)
            assert currNode != None, "The word does not exist in the trie"
            self.nodes[currNode].decreasePrefixes()
        self.nodes[currNode].decreaseWordCount()

    def check(self, word):
        currNode = 1
        for w in word:
            currNode = self.nodes[currNode].getChild(w)
            if currNode == None:
                return 0
        return self.nodes[currNode].wordCount

    def prefixCount(self, word):
        currNode = 1
        for w in word:
            currNode = self.nodes[currNode].getChild(w)
            if currNode == None:
                return 0
        return self.nodes[currNode].prefixes
        

if __name__ == "__main__":
    t = Trie()
    t.add("tree")
    t.add("trie")
    t.add("bye")
    t.add("tr")
    t.remove("trie")
    assert t.check("tr") == 1
    assert t.check("by") == 0
    assert t.check("ten") == 0
    assert t.prefixCount("tr") == 2
