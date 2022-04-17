####################################### Python script to implement a minimum heap ######################################

'''
This script implements a minimum heap data structure that can be used as
a priority queue to get the key with the lowest value.
'''

########################################################################################################################

### Importing required modules

# 3rd party modules
from typing import Union            # Type annotations


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
        self.heap = ["NA"]*(maxsize+1)
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

        # Check if the node is leaf node or 
        # not, if it is a leaf node then do
        # nothing as it serves as the base case.
        if not self.is_leaf_node(position):

            # Now check if any of the child element
            # is smaller than the parent node
            left_child, right_child = self.get_child(position)

            if ((self.heap[left_child] < self.heap[position]) or 
                (self.heap[right_child] < self.heap[position])):
                
                # If left child is smaller than the 
                # right child then swap the left child 
                # with the parent and recursively heapify
                # the position of left child
                if self.heap[left_child] < self.heap[right_child]:
                    self.swap(position, left_child)
                    self.heapify(left_child)

                # Else perform the above steps
                # for the right child.
                else:
                    self.swap(position, right_child)
                    self.heapify(right_child)

        return None


    def insert_node(self, element: Union[int, tuple]) -> None:
        '''
        Function to insert node to a heap.
        ...

        Parameters
        ----------
        element (int or tuple):
            element to be added to the tuple

        Returns
        -------
        None
        '''

        if self.size >= self.maxsize:
            return "No space!!!"

        self.size += 1
        self.heap[self.size] = element

        current_position = self.size
        while (self.heap[current_position] < self.heap[self.get_parent(current_position)]):
            self.swap(current_position, self.get_parent(current_position))
            current_position = self.get_parent(current_position)


    def print_heap(self) -> None:
        '''
        Function to print the elements 
        of the heap.
        ...

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''

        for i in range(1, (self.size//2) + 1):
            parent = self.heap[i]
            left_child = self.heap[2*i]
            right_child = self.heap[2*i + 1]
            print(f"PARENT: {parent}, LEFT CHILD: {left_child}, RIGHT CHILD: {right_child}")

        return None


    def remove_element(self):
        '''
        Function to remove the minium element
        from the heap and return it.
        ...

        Parameters
        ----------
        None

        Returns
        -------
        Minimum element from the heap
        '''

        min_element = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size]
        self.size -= 1
        self.heapify(self.front)


########################################################################################################################


if __name__ == "__main__":

    H = MinimumHeap(15)
    H.insert_node(5)
    H.insert_node(3)
    H.insert_node(17)
    H.insert_node(10)
    H.insert_node(84)
    H.insert_node(19)
    H.insert_node(6)
    H.insert_node(22)
    H.insert_node(9)
    H.print_heap()

    





