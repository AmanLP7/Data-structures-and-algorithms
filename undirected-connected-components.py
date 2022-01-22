##################################### Undirected connected components in a graph #######################################

'''
This script finds the connected components in a given undirected graph using breadth first search.
The run time for this algorithm is O(n+m), where n is the number of nodes and m is number of edges.
'''

########################################################################################################################

### Importing required modules

# System library imports
from queue import Queue                                 # Queue data structure
from pprint import PrettyPrinter                        # Printing a dictionary

# Importing user defined modules
from graph import Graph                                 # Create a grah based on adjacency list


########################################################################################################################

class ConnectedComponents:
    '''
    Class containing methods to find connected components
    in an undirected graph.
    ...

    Attributes
    ----------
    None
    '''

    def __init__(self):
        '''
        Function to instatiate object of the class.
        ...

        Parameters
        ----------
        None
        '''
        ...

    
    def find_components(self, graph: dict) -> None:
        '''
        Function to print connected components of a graph.
        ...

        Parameters
        ----------
        graph (dict):
            A dictionary representing a graph

        Returns
        -------
        None
        '''

        # Creating a dictionary which holds 
        # information about whether a node
        # has been explore or node
        temp = zip(graph.keys(), [False]*len(graph.keys()))
        marker = {x: y for x, y in temp}

        # Creating a queue to temporarily
        # hold the nodes that have been explored
        Q = Queue()

        for node in graph.keys():
            
            if marker[node] is not True:
                Q.put(node)
                marker[node] = True
                print(f"\nExplored first node connected component: {node}")

            while Q.empty() is False:
                node = Q.get()
                for v in graph[node]:
                    if marker[v] is not True:
                        marker[v] = True
                        print(f"Explored node: {v}")
                        Q.put(v)

        return None


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

    components = ConnectedComponents()
    components.find_components(g._graph)
