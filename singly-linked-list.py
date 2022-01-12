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


    def push(self, value: Union[int, float]) -> None:
        '''
        Function to add new node at the front of a singly
        linked list. The time complexity of this operation
        is O(1).
        ...

        Parameters
        ----------
        value (int or float):
            value to be inserted

        Returns
        -------
        None
        '''

        # Create a new node element
        new_node = Node(value)

        # Point the new node to the head of linked list
        new_node.next = self.head

        # Make the value as the new head of linked list
        self.head = new_node 


    def insert_after_node(self, prev_node: object, value) -> Union[None, str]:
        '''
        Function to add a new node after a specified node.
        The time complexity of this function is O(1).
        ...

        Parameters
        ----------
        prev_node (object):
            node object after which the new value will be added
        value (int or float):
            new value to be added

        Returns
        -------
        If prev node is not found then return string else None
        '''

        # Checking of the previous node exists
        if prev_node is None:
            return "Node must exist in the linke list..."

        # Create a new node object
        new_node = Node(value)

        # Point the new node to the next value 
        # of the previous node
        new_node.next = prev_node.next

        # Point the previous node to the new node
        prev_node.next = new_node


    def append(self, data: Union[int, float]) -> Union[None, str]:
        '''
        Function to add a new node to the end of a linked list.
        The time complexity of this operation is O(n), where n
        is the number of nodes in the linked list.
        ...

        Parameters
        ----------
        value (int, float):
            data to be added

        Returns
        -------
        None
        '''

        # Create a new node
        new_node = Node(data)

        # Check if the linked list is empty
        # or not, if empty then make the node
        # the new head of the linked list
        if self.head is None:
            self.head = new_node
            return None

        # Else travel to the last node
        # and point the last node to the 
        # new node
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node

        return None        


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

    # Adding new element at the front
    # of the linked list
    llist.push(4)
    print("Modified list...\n")
    llist.print_linked_list()

    # Adding new element after an
    # existing node
    llist.insert_after_node(second, 7)
    print("Node added in between the linked list...\n")
    llist.print_linked_list()

    # Adding new node at the last of
    # linked list
    llist.append(10)
    print("Node added at the end of linked list...\n")
    llist.print_linked_list()


