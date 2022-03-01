####################################### Python script to implement a minimum heap ######################################

'''
This script implements a minimu heap data structure that can be used as
a priority queue for ascending order
'''

########################################################################################################################

class MinimumHeap:
    '''
    Class containing methods to implement
    minimum heap data structure.
    ...

    Attributes
    ----------

    maxsize (int):
        maximum size of the heap
    front (int):
        start index of the heap
    heap (list):
        list for containing values
    size (int):
        Indicates current size of the heap
    '''

    def __init__(self, maxsize: int) -> None:
        '''
        Function to instantiate class object.
        ...

        Parameters
        ----------
        maxsize (int):
            Maximum size of the heap

        Returns
        -------
        None
        '''

        self.maxsize = maxsize
        self.heap = [0]*(maxsize+1)
        self.front = 1
        self.heap[0] = -float("inf")
        self.size = 0


    def get_parent(self, position: int) -> int:
        '''
        Function to return the position
        of parent element of an element
        at a given position.
        ...

        Parameters
        ----------
        position (int):
            Position of the element whose
            parent has to be found

        Returns
        -------
        Position of the parent element
        '''

        return (position // 2)


    def get_child(self, position: int) -> list:
        '''
        Function to return the position
        of the left child of element at
        the given position.
        ...

        Parameters
        ----------
        position (int):
            Position of the element
            whose left child has to
            be found

        Returns
        -------
        List containing position of left and
        right child. First element of list is
        position of left child and the second 
        one is position of right child.
        '''

        childs = [2*position, 2*position+1]

        return childs


    def is_leaf_node(self, position: int) -> bool:
        '''
        Function to returns whether a position
        is a leaf node or not.
        ...

        Parameters
        ----------
        position (int):
            Position to be checked for being
            leaf node

        Returns
        -------
        True if position is leaf node else false.
        '''

        return (2*position > self.size)


    def swap(self, first: int, second: int) -> None:
        '''
        Function to swap elements at 2 
        positions in a heap.
        ...

        Parameters
        ----------
        first (int):
            position of the first element
        second (int):
            position of the second element

        Returns
        -------
        None
        '''

        self.heap[first], self.heap[second] = self.heap[second], self.heap[first]

        return None


    def heapify(self, position: int) -> None:
        '''
        Function to heapify a given position.
        ...

        Parameters
        ----------
        position (int):
            position of the element
            to be heapified

        Returns
        -------
        None
        '''

        pass