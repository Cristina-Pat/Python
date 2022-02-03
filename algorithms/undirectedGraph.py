from __future__ import unicode_literals
from importlib.resources import path
from operator import ne
from random import random
import graphlib
from typing import Hashable
from graphs import Digraph
from collections import deque

class UndirectedGraph(Digraph):

    #add an undirected edge node1-node2 to the graph
    def addEdge(self, node1: Hashable, node2: Hashable) -> None: 
        super().addEdge(node1, node2) #super() allows to access the methods of the superclass Digraph
        super().addEdge(node2, node1)

    #remove edge node1-node2 from the graph
    def removeEdge(self, node1: Hashable, node2: Hashable) -> None:
        super().removeEdge(node1, node2)
        super().removeEdge(node2, node1)

    #return the graph's edges as a set of pair
    def edges(self) -> set:
        allEdges = set()
        for node1 in self.neighbours:
            for node2 in self.neighbours[node1]:
                if(node2, node1) not in allEdges:
                    allEdges.add((node1, node2))
        return allEdges

    #return all nodes that are adjacent to the node
    def getNeighbours(self, node: Hashable) -> set:
        return self.outNeighbours(node)

    #return the number of edges attached to the node
    def inDegree(self, node: Hashable) -> int:
        return self.outDegree(node)

    #return the number of edges attached to the node
    def degree(self, node: Hashable) -> int:
        return self.outDegree(node)


newGraph = UndirectedGraph()

#return a graph with nodes up x-1 and no edges
def nullGraph(x: int) -> UndirectedGraph:
    graph = UndirectedGraph()
    for node in range(x):
        graph.addNode(node)
    return graph
    
#return a graph with nodes and edges 0-1, 1-2, 2-3 ...
def pathGraph(x: int) -> UndirectedGraph:
    graph = nullGraph(x)
    for node in range(x-1):
        graph.addEdge(node, node+1)
    return graph

#return a graph with nodes 0, 1, ... x-1 and edges 0-1, 1-2, 2-3 ... (n-1)-0
def cycleGraph(x: int) -> UndirectedGraph: # x > 0
    graph = pathGraph(x)
    graph.addEdge(x-1, 0)
    return graph

#return a graph with nodes 0, 1 ... x-1 connected to each other
def completeGraph(x: int) -> UndirectedGraph:
    graph = nullGraph(x)
    for node1 in range(x):
        for node2 in range(node1 + 1, x):
            graph.addEdge(node1, node2)
    return graph

#return a random graph with x nodes
def randomGraph(x: int, prob: float) -> UndirectedGraph:
    graph = nullGraph(x)
    for node1 in range(x):
        for node2 in range(node1 + 1, x):
            if random() < prob: #0 <= prob <= 1
                graph.addEdge(node1, node2) #each edge has the given probability(prob) of existing
    return graph

#return all nodes reachable from start, in order visited
def traversal(graph:Digraph, start: Hashable) -> list:
    visited = [start]
    forProcessing = graph.outNeighbours(start)
    while len(forProcessing) > 0:
        node = forProcessing.pop()
        if node not in visited:
            visited.append(node)
            for neighbour in graph.outNeighbours(node):
                forProcessing.add(neighbour)
    return visited

#return the traversed subgraph when beginning at start
def traversed(graph: Digraph, start: Hashable) -> Digraph:
    visited = Digraph()
    visited.addNode(start)
    forProcessing = set()
    for neighbour in graph.outNeighbours(start):
        forProcessing.add((start, neighbour))
    while len(forProcessing) > 0:
        edge = forProcessing.pop()
        previous = edge[0]
        current = edge[1]
        if not visited.hasNode(current):
            visited.addNode(current)
            visited.addEdge(previous, current)
            for neighbour in graph.outNeighbours(current):
                forProcessing.add(current, neighbour) 
    return visited

#return the subgraph traversed by a breadth-first search
def breadthFirstSearch(graph: Digraph, start: Hashable) -> Digraph:
    visited = Digraph()
    visited.addNode(start)
    forProcessing = deque()
    for neighbour in graph.outNeighbours(start):
        forProcessing.append((start, neighbour))
    while len(forProcessing) > 0:
        edge = forProcessing.popleft()
        previous = edge[0]
        current = edge[1]
        if not visited.hasNode(current):
            visited.addNode(current)
            visited.addEdge(previous, current)
            for neighbour in graph.outNeighbours(current):
                forProcessing.append(current, neighbour)
    return visited

#return the subgraph traversed by a depth-first search
def breadthFirstSearch(graph: Digraph, start: Hashable) -> Digraph:
    visited = Digraph()
    visited.addNode(start)
    forProcessing = []
    for neighbour in graph.outNeighbours(start):
        forProcessing.append((start, neighbour))
    while len(forProcessing) > 0:
        edge = forProcessing.pop()
        previous = edge[0]
        current = edge[1]
        if not visited.hasNode(current):
            visited.addNode(current)
            visited.addEdge(previous, current)
            for neighbour in graph.outNeighbours(current):
                forProcessing.append(current, neighbour)
    return visited


test2 = UndirectedGraph()
test2.addNode('Tom')
test2.addNode('Isa')
test2.addNode('Greg')
test2.addNode('Alex')

test2.addEdge('Tom', 'Isa')
test2.addEdge('Tom', 'Alex')

test2.addEdge('Isa', 'Tom')
test2.addEdge('Isa', 'Alex')

test2.addEdge('Alex', 'Isa')
test2.addEdge('Alex', 'Tom')

print(test2.edges())
print(test2.getNeighbours('Alex'))
print(test2.degree('Tom'))

print(traversal(pathGraph(4), 1)) #start from node 1
print(traversal(cycleGraph(5+1), 0))