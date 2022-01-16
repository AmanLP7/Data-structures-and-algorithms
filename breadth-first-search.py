################################################# Breadth-first-search #################################################

'''
This code implements breadth-first-search algorithm for a graph. The time complexity us O(m+n) where m is number of
edges and n is the number of nodes.
'''

########################################################################################################################

### Importing required modules

# System library imports
from queue import Queue                 # Contains queue data structure
from pprint import PrettyPrinter        # For printing the contents of the graph    

# User defined modules
from graph import Graph         # Create a graph object


########################################################################################################################

class BreadthFirstSearch:
    '''
    Class containing functions to perform a breadth 
    first search on a given graph.
    '''

    def __init__(self):
        '''
        Function to intialise a breadth first search class
        ...

        Parameters
        ----------
        None
        Returns
        -------
        None
        '''

        pass


    def create_queue(self) -> Queue:
        '''
        Function to create a queue which follows 
        FIFO order.
        ...

        Parameters
        ----------
        None

        Returns
        -------
        A Queue() instance
        '''

        return Queue()


    def search(self, graph: dict) -> None:
        '''
        Function to perform breadth first search
        given a graph. The time complexity of this 
        operation is O(m+n).
        ...

        Parameters
        ----------
        graph (dict):
            graph to be searched

        Returns
        -------
        None
        '''

        # Creating a dictionary holding information
        # about whether a node is explored or not
        temp = zip(graph.keys(), [False]*(len(graph.keys())))
        marker = {x:y for x, y in temp}
        
        # Creating a queue to temporarily hold
        # nodes that have been explored
        Q = self.create_queue()

        # Put the first item of the graph in the
        # queue and mark it as explored
        for node in graph.keys():
            Q.put(node)
            marker[node] = True
            print(f"Explored node: {node}")
            break

        # Run the while loop until Q
        # runs out of nodes
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
    pretty_print.pprint(g._graph)

    print("\nPerforming a breadth first search on the graph ...\n")

    BFS = BreadthFirstSearch()
    BFS.search(g._graph)
