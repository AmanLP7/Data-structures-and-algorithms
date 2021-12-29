###################################### Python script to find minimum cut in a graph ####################################

''' 
This is a python script to find minmum number of cuts in graph using Karger's random contraction algorithm.
'''

########################################################################################################################

### Importing required modules

# System library imports 
import random                   # Contain functions to make random selections

########################################################################################################################

class KargersMinCut:
    ''' 
    Class containing functions to find minimum number of cuts in a graph
    '''

    def __init__(self):
        ''' 
        Function to initialise a graph data structure
        ...

        Paramaters
        ----------
        None

        Returns
        -------
        None
        '''

        self.graph = {}


    def create_graph(self, file: str, delimeter: str = " ") -> dict:
        ''' 
        Function to create a graph given and adjacency list
        ...

        Parameters
        ----------
        file (str):
            address of the text file containing adjacency list
        delimeter (str):
            delimeter used to seperate values

        Returns
        -------
        A graph respresented as a dictionary
        '''

        with open(file, "r") as adj:
            for line in adj:
                l = list(map(int, line.strip().split(delimeter)))
                self.graph[l[0]] = l[1:]
        return self.graph


    def choose_random_edge(self, graph: dict) -> tuple:
        '''
        Function to choose a random edge
        ...

        Parameters
        ----------
        graph (dict):
            A graph as a dictionary

        Returns
        -------
        A tuple containing nodes connected by the edge
        '''
        
        node1 = random.choice(list(graph.keys()))
        node2 = random.choice(graph[node1])

        return (node1, node2)


    def random_contraction(self, graph: dict) -> int:
        '''
        Function find the minimum number of cuts in a graph
        using random contraction.
        ...

        Parameters
        ----------
        graph (dict):
            A graph as dictionary

        Returns
        -------
        Minimum number of cuts
        '''

        # Keep contracting the edges until
        # no more than 2 nodes remain
        while len(graph) > 2:
            
            # Choose random edge
            v1, v2 = self.choose_random_edge(graph)

            # Add elements of v2 to v1, for each node 
            # connected to v2, delete connection to v2
            # and add connection to v1
            graph[v1].extend(graph[v2])
            del graph[v2] 
            for node, _ in graph.items():
                graph[node] = [v1 if x == v2 else x for x in graph[node]]

            # Remove self loops for node v1
            graph[v1] = [x for x in graph[v1] if x != v1]

        minimum_cuts = len(graph[list(graph.keys())[0]])

        return minimum_cuts



########################################################################################################################


if __name__ == '__main__':

    kargers = KargersMinCut()

    # List to hold minimum cuts for each iteration
    cuts = []

    for _ in range(300):
        graph = kargers.create_graph("test.txt", delimeter=" ")
        min_cuts = kargers.random_contraction(graph)
        cuts.append(min_cuts)
        print(f"Iteration {_} : cuts: {min_cuts}...\n")
    
    print(f"Minimum number of cuts: {min(cuts)}\n")