###################################### This scripts implement Djikstra's algorithm #####################################

'''
This script implements Djikstra's algorithm to find the shortest path in a graph from a given node. 
The time complexity of this algorithm is O(mn), where n is the number of nodes and m is the number of edges.
'''

########################################################################################################################

### Importing required modules

# System library imports
from pprint import PrettyPrinter        # Print a graph
from datetime import datetime           # Working with date and time

# User defined modules
from graph import Graph                 # Create a graph

# 3rd party libraries
from typing import Union                # Type annotations

########################################################################################################################

class DjikstraAlgorithm:
    '''
    Class containing methods to implement
    Djikstra's algorithm.
    ...

    Attributes
    ----------
    marker (dict):
        dictionary containing information about
        whether a nodes has been explored or not
    distance (dict):
        dictionary where key is the node and
        value is the shortest distance from the
        given node 
    '''

    def __init__(self, graph: dict) -> None:
        '''
        Function to instantiate an object of class
        ...

        Parameters
        ----------
        graph (dict):
            a dictionary representing a graph
        '''

        self.graph = graph
        self.marker = {}
        self.distance = {}

        for key in self.graph.keys():
            self.marker[key] = False
            for node in self.graph[key]:
                self.marker[node] = False

        self.distance = {x: 0 for x in self.marker.keys()}


    def get_shortest_distance(self, start_node: Union[int, str]) -> dict:
        '''
        Function to find shortest distance of a node
        from start node.
        ...

        Parameters
        ----------
        start_node (int or str):
            node to start calculating distance from

        Returns
        -------
        A dictionary where key is the node
        and value is the shortest distance 
        from the start node.
        '''

        # Initialising the distance of start node
        # from itself as 0 and marking it as explored
        self.marker[start_node] = True
        self.distance[start_node] = 0

        for node in self.graph.keys():
            distance = float("inf")
            for w in self.graph[node]:
                if w[1] < distance:



########################################################################################################################

if __name__ == "__main__":

    # Reading the adjacency list
    connections = []
    with open("test.txt", "r") as graph_data:
        for line in graph_data:
            connection_list = line.strip().split(" ")
            node = connection_list[0]
            edges = [x.split(",") for x in connection_list[1:]]
            edges = [(x[0], int(x[1])) for x in edges]
            connections.append((node, edges))

    g = Graph(connections, directed=True)

    pretty_print = PrettyPrinter()
    pretty_print.pprint(g._graph)

