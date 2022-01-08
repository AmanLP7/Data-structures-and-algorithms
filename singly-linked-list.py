#################################################### Singly linked list ################################################

''' 
Python program to implement singly-linked list.
'''

########################################################################################################################

### Importing required modules

# 3rd party modules
from typing import Union                    # Specify type of data input or returned by function

########################################################################################################################

class Node:
    ''' 
    Class to represent a node in singly-linked list
    '''

    def __init__(self, data: Union[int, float]):
        ''' 
        Function to create a node object
        ...

        Parameters
        ----------
        data (int or float):
            value of the node

        Returns
        -------
        None
        '''

        self.data = data
        self.next = None


class LinkedList:
    '''
    Class to create a linked list object
    '''

    def __init__(self):
        '''
        Function to initailse a linked list
        ...

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''

        self.head = None


    def print_linked_list(self):
        '''
        Function to traverse and print elements of the linked list
        ...

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''

        element = self.head
        while (element):
            print(element.data)
            element = element.next

########################################################################################################################

if __name__ == '__main__':

    # Initialise a linked list object
    llist = LinkedList()

    # Filling linked list with element
    # and creating nodes    
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    # Connecting nodes together
    llist.head.next = second
    second.next = third

    llist.print_linked_list()


