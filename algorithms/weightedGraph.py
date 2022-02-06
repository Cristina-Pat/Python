import math
from turtle import st
from typing import Hashable
from graphs import Digraph

weightedGraph = {
    0: {1: 15, 2: 10, 3: 5}, 
    1: {0: 15, 2: 30, 3: 5}, 
    2: {0: 10, 1: 30, 3: 10},
    3: {0: 5, 1: 5, 2: 10}
}

class WeightedDigraph(Digraph):
    
    #add the node to the graph
    def addNode(self, node: Hashable) -> None: 
        self.neighbours[node] = dict() #a map of out-neighbours to weights

    #add edge start->end with weight to the graph
    def addEdge(self, start: Hashable, end: Hashable, weight: float) -> None: 
        #preconditions:self.hadNode(start) and self.hadNode(end) and start != end
        self.neighbours[start][end] = weight

    #return the weight of edge start -> end or infinit if it doesn't exist 
    def weight(self, start: Hashable, end: Hashable) -> float:
        if self.hasEdge(start, end):
            return self.neighbours[start][end]
        else:
            return math.inf

    #remove edge start->end from the graph
    def removeEdge(self, start: Hashable, end: Hashable) -> None: 
        #preconditions:self.hadNode(start) and self.hadNode(end)
        if self.hasEdge(start, end):
            self.neighbours[start].pop(end)

    #return the graph's edges as a set of (start, end, weight)
    def edges(self) -> set: 
        allEdges = set ()
        for start in self.neighbours:
            for (end, weight) in self.neighbours[start].items():
                allEdges.add((start, end, weight))
        return allEdges

    #return the out-neighbours of the node
    def outNeighbours(self, node: Hashable) -> set: 
        return set(self.neighbours[node].keys()) # return a copy
