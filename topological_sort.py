############################################## Topological sorting in graph ############################################

'''
This is a python script to implement topological sorting given a directed acyclic graph.
The time complexity of this operation is O(n+m), where n is the number of nodes and
m is the number of edges.
'''

########################################################################################################################


### Importing required modules

# System library imports
from pprint import PrettyPrinter                            # Printing a graph

# 3rd party modules
from typing import Union                                    # Type hints

# User defined modules
from graph import Graph                                     # Create a graph
from recursive_depth_first_search import DepthFirstSearch   # Depth first search


########################################################################################################################


class TopologicalSort:
    '''
    Class containing methods to implement topological sort.
    ...

    Attributes
    ----------
    order (dict):
        Dictionary where key is the node and value
        is its order.
    label (int):
        Label representing the order of the node
    ''' 

    def __init__(self, graph: dict):
        '''
        Function to instantiate a class object.
        ...

        Parameters
        ----------
        graph (dict):
            A graph represented as a dictionary

        Returns
        -------
        None
        '''

        self.graph = graph
        self.order = {}
        for key in self.graph.keys():
            self.order[key] = None
            for node in self.graph[key]:
                self.order[node] = None
        self.label = len(self.order.keys())
        self.marker = {x: False for x in self.order.keys()}


    def depth_first_search(
                        self, 
                        graph: dict,
                        start_vertex: Union[int, float, str]
                        ) -> None:
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

        # Marking the node as explored
        self.marker[start_vertex] = True
        
        # Recursive searching through
        # all the edges of node
        if graph.get(start_vertex) is not None:
            for node in graph[start_vertex]:
                if self.marker[node] is not True:
                    self.depth_first_search(graph, node)

        # Storing order of node and
        # decrementing label by 1
        self.order[start_vertex] = self.label
        self.label -= 1


    def topological_sort(self) -> dict:
        '''
        Function to sort nodes of a graph in
        topological order.
        ...

        Parameters
        ----------
        None

        Returns
        -------
        A dictionary where key is the node
        and value is the topological order
        '''

        # Iterating through all the nodes
        for node in self.graph.keys():
            if self.marker[node] is False:
                self.depth_first_search(self.graph, node)

        return self.order


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

    # Creating a graph
    g = Graph(connections, directed=True)

    # Print the graph
    pretty_print = PrettyPrinter()
    pretty_print.pprint(g._graph)

    graph_sort = TopologicalSort(g._graph)

    order = graph_sort.topological_sort()

    pretty_print.pprint(graph_sort.order)

