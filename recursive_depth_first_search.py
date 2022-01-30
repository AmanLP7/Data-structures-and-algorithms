############################################ Recursive depth first search ##############################################

'''
This script implements depth first search for a graph using recursion. The run time complexity for this operation 
is O(m+n), where m is the number of edges and n is the number of nodes.
'''

########################################################################################################################

### Importing required modules

# System library imports
from pprint import PrettyPrinter            # Printing a dictionary

# 3rd party libraries
from typing import Union                    # Provide type hints

# User define modules
from graph import Graph                     # Create a graph


########################################################################################################################


class DepthFirstSearch:
    '''
    Class containing methods to implement depth first search.
    ...

    Attributes
    ----------
    marker (dict):
        a dictionary where key is the node
        and value is a boolean respresenting
        whether the node has been explored 
        or not.
    '''

    def __init__(self):
        '''
        Function to instantiate object of the class.
        ...

        Parameters
        ----------
        None
        '''

        self.marker = None


    def create_marker(self, graph: dict) -> dict:
        '''
        Function to create a dictionary of nodes
        given a graph where key is node and
        value is a boolean representing whether
        a node has been explored or not.
        ...

        Parameters
        ----------
        graph (dict):
            a graph represented as a dict

        Returns
        -------
        A dictionary respresenting the status
        of graph nodes
        '''
        
        # Creating a dictionary to hold information
        # whether a node has been explored or not
        temp = zip(graph.keys(), [False]*len(graph.keys()))
        self.marker = {x: y for x, y in temp}


    def search(self, graph: dict, start_vertex: Union[int, float, str]) -> None:
        '''
        Function to perform depth first search
        in a graph. The time complexity of this
        operation is O(m+n) where m is number 
        of edges and n is the number of nodes.
        ...

        Parameters
        ----------
        graph (dict):
            a dictionary representing a graph

        Returns
        -------
        None
        '''

        self.marker[start_vertex] = True
        
        for node in graph[start_vertex]:
            if self.marker[node] is not True:
                self.search(graph, node)
        
        print(f"Explored node: {start_vertex}")

########################################################################################################################


if __name__ == "__main__":

    # Reading the adjacency list
    connections = []
    with open("test.txt", "r") as data:
        for line in data:
            connection_list = line.strip().split(" ")
            node = connection_list[0]
            edges = list(connection_list[1:])
            connections.append((node, edges))

    # Create a graph
    g = Graph(connections)

    pretty_print = PrettyPrinter()
    pretty_print.pprint(g._graph)

    DFS = DepthFirstSearch()
    DFS.create_marker(g._graph)

    start = list(g._graph.keys())[0]
    DFS.search(g._graph, start)
        

