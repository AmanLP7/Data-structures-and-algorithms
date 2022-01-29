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

        self.order = {x: None for x, y in graph.items()}
        self.label = len(graph.keys())


    


    

