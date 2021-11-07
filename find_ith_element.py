########################################## Python script to find ith smallest element ##################################

'''
Python script to find ith smallest element in an array. Time complexity is O(n).
'''

########################################################################################################################

### Importing required modules

# System library imports
from random import randint          # To chose a random element in a given range

# 3rd party libraries


########################################################################################################################

class FindElement:
    '''
    Class containing methods to find ith smallest element in an array
    ...

    Attributes
    ----------
    None
    '''

    def __init__(self):
        '''
        Function to instantiate class object
        ...

        Parameters
        ----------
        None 
        '''

        pass


    def partition(self, arr: list, l: int, r: int) -> list:
        '''
        Function to partition the array around a chosen
        pivot element, the pivot element is chose randomly
        and then the array is partitioned based on quick
        sort algorithm
        ...

        Parameters
        ----------
        arr (list):
            list of elements to be partitioned
        l (int):
            left most index
        r (int):
            right most index

        Returns
        -------
        A tuple containing:
        1. Partitioned array
        2. Left most index of array
        3. Position of pivot element
        4. Right most index of array
        '''

        # Choose a random index from the array
        # and swap the first element of the array
        # with the element at the chosen index
        index = randint(l, r-1)
        arr[l], arr[index] = arr[index], arr[l]

        # Choose the first element of the array as pivot
        pivot = arr[l]
 
        # Initialise the indices
        i = l+1

        # Iterate through the elements of the array
        # swap the jth element with ith element if 
        # jth element is smaller than or equal
        # to the pivot element
        for j in range(l+1, r):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        
        # Swap first element of array 
        # with element at (i-1)th index
        arr[l], arr[i-1] = arr[i-1], arr[l]

        return (arr, l, i-1, r)


    def random_select(self, arr: list, l: int, r: int, element: int) -> 

    