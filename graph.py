#################################### Python script to create a graph data structure ####################################

'''
This is a python script that creates a graph data structure given a list of connections represented as
a tuple of nodes.
'''

########################################################################################################################

### Import required modules

# System library imports
from pprint import PrettyPrinter        # Python pretty printer
from collections import defaultdict     # Dictionaries with default values


########################################################################################################################

class Graph:
    '''
    Class to create graph objects in python, directed or undirected
    '''

    def __init__(self, connections, directed=False):
        '''
        Function to initialise a graph object
        ...
        Parameters
        ----------
        connections (list):
            list of tuples of connected nodes
        directed (boolean):
            whether the graph is directed or not

        Returns
        -------
        None
        '''

        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)


    def add_connections(self, connections: list) -> None:
        ''' 
        Function to add connection to the graph
        ...

        Parameters
        ----------
        connections (list):
            list of connections represented as adjacency matrix

        Returns
        -------
        None
        '''

        for connection in connections:
            node1 = connection[0]
            for node in connection[1]:
                self.add(node1, node)

    
    def add(self, node1: int, node2: int) -> None:
        ''' 
        Function to connect node 1 to node 2,
        where node 1 is the dictionary key and
        node 2 is appended to the value which is
        a set of unique nodes connected to node 1
        ...

        Parameters
        ----------
        node1 (int):
            node 1 
        node2 (int):
            node 2

        Returns
        -------
        None
        '''

        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)


    def remove(self, node: int) -> None:
        ''' 
        Function to remove a node and its references
        ...

        Parameters
        ----------
        node (int):
            node to be deleted from the graph
        '''

        for vertex, connections in self._graph.items():
            connections.discard(node)

        try:
            del self._graph[node]
        except KeyError:
            pass






########################################################################################################################

if __name__ == '__main__':

    # Reading the adjacency list
    connections = []
    with open("D:/My github/Algorithms-divide-conquer/Assignment-4/kargerMinCut.txt", "r") as graph_data:
        for line in graph_data:
            connection_list = line.strip().split("\t")
            node = int(connection_list[0])
            edges = list(map(int, connection_list[1:]))
            connections.append((node, edges))

    g = Graph(connections)

    pretty_print = PrettyPrinter()
    pretty_print.pprint(g._graph[200]) 

    g.remove(200)

    pretty_print.pprint(g._graph[200])
