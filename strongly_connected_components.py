###################################### Script to find strongly connected components ####################################

'''
This is a python script to find strongly connected components in a graph. The time complexity for 
this operation is O(m+n) where m is the number of edges and n is the number of nodes.
'''

########################################################################################################################

### Importing required modules

# System library imports
from pprint import PrettyPrinter    # For printing graphs

# User defined modules
from graph import Graph             # Create a graph


########################################################################################################################

class SCC:
    '''
    Class containing methods to calculate strongly
    connected components.

    Attributes
    ----------
    t (int):
        finishing time of a node
    '''

    def __init__(self, graph: dict) -> None:
        '''
        Function to instantiate object of class.
        ...

        Parameters
        ----------
        graph (dict):
            A dictionary representing a graph
        
        Returns
        -------
        None
        '''

        self.graph = graph
        self.t = 0


    def reverse(self) -> dict:
        '''
        Function to reverse a graph.
        ...

        Parameters
        ----------
        None

        Returns
        -------
        A dictionary representing reversed graph
        '''
        connections = []

        for key, value in self.graph.items():
            for v in value:
                connections.append((v, key))

        reverse_graph = Graph(connections, directed=True)

        return reverse_graph._graph
        


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

    scc = SCC(g._graph)

    a = scc.reverse()

    pretty_print.pprint(a)

