###################################### Script to find strongly connected components ####################################

'''
This is a python script to find strongly connected components in a graph. The time complexity for 
this operation is O(m+n) where m is the number of edges and n is the number of nodes.
'''

########################################################################################################################

### Importing required modules

# System library imports
from pprint import PrettyPrinter        # For printing graphs
from queue import LifoQueue             # A LIFO queue
from collections import defaultdict     # Create dictionary with default element

# User defined modules
from graph import Graph             # Create a graph


########################################################################################################################

class SCC:
    '''
    Class containing methods to calculate strongly
    connected components.

    Attributes
    ----------
    finish_time (stack):
        contains order of nodes by finishing time
    marker (dict)
        a dictionary to hold information about
        whether a node has beeen explored or not,
        a node may be marked as "white": not explored,
        "grey": in progress, "black": explored
    all_children_discovered (boolean):
        variable representing the status of node
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
        self.finishing_time = LifoQueue()
        self.marker = {}

        for key in self.graph.keys():
            self.marker[key] = "white"
            for node in self.graph[key]:
                self.marker[node] = "white"

        
        self.stack = LifoQueue()
        self.all_children_discovered = None
        self.length_of_components = defaultdict(lambda: 1)


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


    def first_pass(self, graph:dict, node: int) -> None:
        '''
        Function to perform depth first search and assign a
        finishing time to nodes. The algorithm a queue to 
        temporarily store nodes while searching.
        ...

        Parameters
        ----------
        graph (dict):
            a dictionary representing a graph
        node (int):
            first node to start search with

        Returns
        -------
        None
        '''

        # Marking input node as explored
        # and pushing it into stack
        self.stack.put(node)

        # Run the while loop until
        # stack runs out of nodes
        while self.stack.empty() is not True:

            # Get the latest element
            n = self.stack.get()

            # If node is not fully explored
            # append it back to the stack
            # and explore the child nodes
            if self.marker[n] != "black":
                self.stack.put(n)

                # If marker of node is white
                # set it to grey
                if self.marker[n] == "white":
                    self.marker[n] = "grey"

                # Set variable representing whether
                # all children nodes are discovered
                # as True
                self.all_children_discovered = True

                # Exploring edges of the node n
                if graph.get(n) is not None:
                    for v in graph[n]:
                        if self.marker[v] == "white":
                            self.stack.put(v)
                            self.all_children_discovered = False

                # If all the children of the node has been discovred
                # pop the node from the stack and append to the 
                # stack holding the order if nodes based on their
                # finishing times
                if self.all_children_discovered:
                    self.marker[n] = "black"
                    self.finishing_time.put(n)
                    self.stack.get()

            else:
                pass


    def second_pass(self, leader_node: str) -> None:
        '''
        Function to implement second pass to find the
        length of each strongly connected component.
        The time complexity of this operation is O(m+n).
        ...

        Parameters
        ----------
        leader_node (str):
            node to start the search with

        Returns
        -------
        None
        '''

        # Push the leader node in the stack
        node = leader_node
        self.stack.put(node)
        self.marker[node] = "black"

        # Iterate while the stack is not empty
        while self.stack.empty() is not True:

            # Get the last node
            node = self.stack.get()

            # Explore edges of node
            if self.graph.get(node) is not None:
                for edge in self.graph[node]:
                    if self.marker[edge] == "white":
                        self.marker[edge] = "black"
                        self.stack.put(edge)
                        self.length_of_components[leader_node] += 1

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

    # Creating a graph
    g = Graph(connections, directed=True)

    # Print the graph
    pretty_print = PrettyPrinter()

    # Creating a class object
    scc = SCC(g._graph)

    # Reversing the graph
    reverse_graph = scc.reverse()

    # Calculating the finishng times
    for node in range(len(reverse_graph.keys()), 0, -1):
        scc.first_pass(reverse_graph, str(node))

    # Marking all the nodes as explored
    scc.marker = {x:"white" for x in scc.marker.keys()}

    # Performing second pass in the original graph
    while scc.finishing_time.empty() is not True:
        element = scc.finishing_time.get()
        scc.second_pass(str(element))

    pretty_print.pprint(scc.length_of_components)

