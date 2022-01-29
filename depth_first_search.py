################################################### Depth first search #################################################

'''
This python script implements depth first search for a graph using stacks. The time complexity of
the algorithm is O(n+m), where n is the number of nodes and m is the number of edges.
'''

########################################################################################################################

### Importing required modules

# System library imports
from queue import LifoQueue             # Queue with stack functionality
from pprint import PrettyPrinter        # Printing a dictionary

# User defined modules
from graph import Graph                 # Creating a graph


########################################################################################################################


class DepthFirstSearch:
    '''
    Class containing modules to implement depth first search.
    ...

    Attributes
    ----------
    None
    '''

    def __init__(self):
        '''
        Function to instantiate an object of the class.
        ...

        Parameters
        ----------
        None
        '''

        pass


    def search(self, graph: dict) -> None:
        '''
        Function to perform depth first
        search given a graph. The time
        complexity of the operation is
        O(n+m).
        ...

        Parameters
        ----------
        graph (dict):
            A dictionary representing a graph
        
        Returns
        -------
        None
        '''

        # Creating a dictionary holding information
        # about whether a node is explored or not
        temp = zip(graph.keys(), [False]*len(graph.keys()))
        marker = {x: y for x, y in temp}

        # Creating a stack to temporarily hold
        # nodes that have been explored
        stack = LifoQueue()

        # Put the first node of graph
        # in stack and mark it as explored
        for node in graph.keys():
            stack.put(node)
            marker[node] = True
            print(f"Explore node: {node}")
            break

        # Run the while loop until stack
        # runs out of the nodes
        while stack.empty() is not True:
            node = stack.get()
            for v in graph[node]:
                if marker[v] is not True:
                    marker[v] = True
                    print(f"Explored node: {v}")
                    stack.put(v)

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
    pretty_print.pprint(g._graph)

    DFS = DepthFirstSearch()
    DFS.search(g._graph)

