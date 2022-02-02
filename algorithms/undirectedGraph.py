from typing import Hashable
from graphs import Digraph

class UndirectedGraph(Digraph):

    #add an undirected edge node1-node2 to the graph
    def addEdge(self, node1: Hashable, node2: Hashable) -> None: 
        super().addEdge(node1, node2) #super() allows to access the methods of the superclass Digraph
        super().addEdge(node2, node1)

    #remove edge node1-node2 from the graph
    def removeEdge(self, node1: Hashable, node2: Hashable) -> None:
        super().removeEdge(node1, node2)
        super().removeEdge(node2, node1)

    def edges(self) -> set:
        allEdges = set()
        for node1 in self.neighbours:
            for node2 in self.neighbours[node1]:
                if(node2, node1) not in allEdges:
                    allEdges.add((node1, node2))
        return allEdges