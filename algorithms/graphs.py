from typing import Hashable


nodes = ['Tom', 'Isa', 'Greg', 'Alex'] #undirected graph

edges_matrix =[ #adjacency matrix
    [False, True, False, True], #neighbours of node 0 (Tom): node 1 and 3
    [True, False, False, True], #neighbours of node 1 (Isa): node 0 and 3
    [False, False, False, False], #neighbours of node 2 (Greg): none
    [True, True, False, False] #neighbours of node 3 (Alex): node 0 and 1
]

edges_list = [  #lookup table of sequences
    [1, 3], #neighbours of node 0 - Tom
    [0, 3], #neighbours of node 1 - Isa
    [],     #neighbours of node 2 - Greg
    [0, 1]  #neighbours of node 3 - Alex
]

hash_table = { #store the undirected graph in dictionary, both the nodes and their neighbours
    'Tom': ['Isa', 'Alex'], #every undirected edge is represented twice
    'Isa': ['Tom', 'Alex'],
    'Greg': [], 
    'Alex': ['Tom', 'Isa']
}

hash_table_digraph = { # keys - nodes, values - out-neighbours
    1: [2], #out-neighbours of 1: 2
    2: [1], #out-neighbours of 1: 1
    3: [], #out-neighbours of 3: none
    4:[1, 2] #out-neighbours of 4: 1 and 2
}

class Digraph:
    """A directed graph with hashable node objects.
    Edges are between differents nodes. There is at most one edge from one to another.
    """

    def __init__(self):
        self.neighbours = dict() #a map of nodes to their out-neighbours

    def hasNode(self, node: Hashable) -> bool: #return True if the graph has the node
        return node in self.neighbours

    def hasEdge(self, start: Hashable, end: Hashable) -> bool: #return true only if edge start->end exists
        return end in self.neighbours[start] #preconditions: self.hasNode(start) and self.hasNode(end)

    def addNode(self, node: Hashable) -> None: #add the node to the graph
        self.neighbours[node] = set() #preconditions:not self.hasNode(node)

    def addEdge(self, start: Hashable, end: Hashable) -> None: #add edge start->end to the graph
        #preconditions:self.hadNode(start) and self.hadNode(end) and start != end
        self.neighbours[start].add(end)

    def removeEdge(self, start: Hashable, end: Hashable) -> None: #remove edge start->end from the graph
        #preconditions:self.hadNode(start) and self.hadNode(end)
        self.neighbours[start].discard(end)

    def removeNode(self, node:Hashable) -> None: #remove the node and all its edges
        self.neighbours.pop(node)
        for start in self.neighbours:
            self.removeEdge(start, node)

    def nodes(self) -> set: #return the graph's nodes
        allNodes = set()
        for node in self.neighbours:
            allNodes.add(node)
        return allNodes

    def edges(self) -> set: #return the graph's edges as a set of pairs(start, end)
        allEdges = set ()
        for start in self.neighbours:
            for end in self.neighbours[start]:
                allEdges.add((start, end))
        return allEdges

    def outNeighbours(self, node: Hashable) -> set: #return the out-neighbours of the node
        return set(self.neighbours[node]) # return a copy

    def inNeighbours(self, node: Hashable) -> set: #return the in-neighbours of the node
        startNodes = set()
        for start in self.outNeighbours(node):
            if self.hasEdge(start, node):
                startNodes.add(start)
        return startNodes

    def outDegree(self, node: Hashable) -> int: #return the number of out-neighbours of the node
        return len(self.neighbours[node])

    def inDegree(self, node: Hashable) -> set: #return the number of in-neighbours of the node
        return len(self.inNeighbours(node))

    def getNeighbours(self, node: Hashable) -> set: #return the in and out-neighbours of the node
        return self.outNeighbours(node).union(self.inNeighbours(node))

    def degree(self, node: Hashable) -> int: #return the in and out-edges of the node
        return self.inDegree(node) + self.outDegree(node)


test = Digraph()
test.addNode(1)
test.addNode(2)
test.addNode(3)
test.addNode(4)
test.addEdge(1, 2)
test.addEdge(2, 1)
test.addEdge(4, 1)
test.addEdge(4, 2)
nodes = test.nodes()
edges = test.edges()

print(test.getNeighbours(4))

print(test.degree(2))
print(test.outDegree(2))
print(test.outNeighbours(4))

print(test.inNeighbours(4))
print(test.inNeighbours(2))
for x in test.neighbours:
    print(x)

print(nodes)
print(edges)





