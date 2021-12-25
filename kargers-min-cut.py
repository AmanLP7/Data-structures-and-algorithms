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


    def create_graph(self, file: str) -> dict:
        ''' 
        Function to create a graph given and adjacency list
        ...

        Parameters
        ----------
        file (str):
            address of the text file containing adjacency list

        Returns
        -------
        A graph respresented as a dictionary
        '''

        with open(file, "r") as adj:
            for line in adj:
                l = list(map(int, line.strip().split("  ")))
                self.graph[l[0]] = l[1:]

        return self.graph


    def choose_random_edge(self) -> tuple:
        '''
        Function to choose a random edge
        ...

        Parameters
        ----------
        None

        Returns
        -------
        A tuple containing nodes connected by the edge
        '''
        
        node1 = random.choice(list(self.graph.keys()))
        node2 = random.choice(self.graph[node1])

        return (node1, node2)


    def random_contraction(self) -> int:
        '''
        Function find the minimum number of cuts in a graph
        using random contraction.
        ...

        Parameters
        ----------
        None

        Returns
        -------
        Minimum number of cuts
        '''

        # Keep contracting the edges until
        # no more than 2 nodes remain
        while len(self.graph) > 2:
            
            # Choose random edge
            v1, v2 = self.choose_random_edge()

            # Add elements of v2 to v1, for each node 
            # connected to v2, delete connection to v2
            # and add connection to v1
            self.graph[v1].extend(self.graph[v2])
            for node in self.graph[v2]:
                self.graph[node].remove(v2)
                self.graph[node].append(v1)

            # Delete node v2
            del self.graph[v2]

            # Remove self loops for node v1
            while v1 in self.graph[v1]:
                self.graph[v1].remove(v1)

        minimum_cuts = len(self.graph[list(self.graph.keys())[0]])

        return minimum_cuts



########################################################################################################################


if __name__ == '__main__':

    kargers = KargersMinCut()

    G = kargers.create_graph("test.txt")

    cuts = []

    for _ in range(1000):
        min_cuts = kargers.random_contraction()
        cuts.append(min_cuts)
    
    print(set(cuts))