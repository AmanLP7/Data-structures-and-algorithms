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
        while (element.next):
            print(element.data)
            element = element.next

        # Print the last element 
        print(element.data)


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
            return "Node must exist in the linked list..."

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


    def delete_node(self, key: Union[int, float]) -> None:
        '''
        Function to delete a node from the linked list
        ...

        Parameters
        ----------
        key (int, float):
            key to be deleted

        Returns
        -------
        None
        ''' 

        # Save head node in a variable
        temp_node = self.head

        # Check if linked list is empty
        if temp_node is None:
            return None

        # If head node is the key that is
        # supposed to be deleted
        if temp_node.data == key:
            self.head = temp_node.next
            temp_node = None
            return

        # Traversing the linked list to
        # find the key to be deleted
        while (temp_node.next):
            if temp_node.data == key:
                break
            prev_node = temp_node
            temp_node = temp_node.next

        # If key is not present
        if temp_node is None:
            return None

        # Linking node previous to the
        # key to the node next to key
        # and delete the node
        if temp_node.data == key:
            prev_node.next = temp_node.next
            temp_node = None

        return None


    def delete_position(self, position: int) -> None:
        '''
        Function to delete a node from a linked 
        list given a position and return the
        corresponding element
        ...

        Parameters
        ----------
        position (int):
            index of the node to be deleted

        Returns
        -------
        Key at the position to be deleted     
        '''

        # Check if the list is empty
        if self.head is None:
            return None

        # If the position is the head 
        # then make node next to the 
        # head as the new head and delete
        # the head node
        if position == 0:
            temp_node = self.head
            self.head = self.head.next
            return temp_node.data

        index = 0
        current = self.head
        prev = self.head
        temp_node = self.head

        while (current):
            if index == position:
                temp_node = current.next
                break
            prev = current
            current = current.next
            index += 1

        prev.next = temp_node

        return current.data



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

    # Adding new element after an
    # existing node
    llist.insert_after_node(second, 7)

    # Adding new node at the last of
    # linked list
    llist.append(10)
    print("Linked list elements...\n")
    llist.print_linked_list()

    # Deleting the element based on given position
    deleted_element = llist.delete_position(5)
    print(f"Element deleted from the position {5}: {deleted_element}")
    print("Linked list after deletion...\n")
    llist.print_linked_list()