#################################################### Shortest-path #######################################3#############

'''
This code calculates the shortest path between given nodes for a graph. The time complexity us O(m+n) where m is number 
of edges and n is the number of nodes.
'''

########################################################################################################################

### Importing required modules

# System library imports
from queue import Queue                 # Contains queue data structure
from pprint import PrettyPrinter        # For printing the contents of the graph    

# User defined modules
from graph import Graph         # Create a graph object


########################################################################################################################

class ShortestPath:
    '''
    Class containing functions to find shortest
    path between two nodes of a graph
    '''

    def __init__(self):
        '''
        Function to intialise a shortest path class
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


    def distance(self, graph: dict, node1: str, node2: str) -> int:
        '''
        Function to find shortest path between two nodes
        of given graph. The time complexity of this operation
        is O(m+n).
        ...

        Parameters
        ----------
        graph (dict):
            graph containing the nodes
        node1 (str):
            first node
        node2 (str):
            second node

        Returns
        -------
        Distance between first and the second node
        '''

        # Creating a dictionary holding information
        # about whether a node is explored or not
        temp = zip(graph.keys(), [False]*(len(graph.keys())))
        marker = {x:y for x, y in temp}
        temp = zip(graph.keys(), [float("inf")]*(len(graph.keys())))
        dist = {x: float("inf") for x, y in temp}
        
        # Creating a queue to temporarily hold
        # nodes that have been explored
        Q = self.create_queue()

        # Mark node1 as explored and
        # set its distance from itself
        # as 0, and add node1 to queue
        marker[node1] = True
        dist[node1] = 0 
        Q.put(node1)

        # Run the while loop until Q
        # runs out of nodes
        while Q.empty() is False:
            node = Q.get()
            for v in graph[node]:
                if marker[v] is not True:
                    marker[v] = True
                    dist[v] = dist[node] + 1
                    Q.put(v)

        return dist[node2]
            


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

    path = ShortestPath()
    shortest_path = path.distance(g._graph, "s", "d")

    print(f"The shortest path is: {shortest_path}")
