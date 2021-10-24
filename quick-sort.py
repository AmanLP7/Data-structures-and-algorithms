######################################## Python script to implement quick sort ########################################

'''
Python program to implement quick sort, time complexity is n*log(n)
'''

#######################################################################################################################

### Importing required modules

# System library imports
from random import randint                      # To choose a random element


#######################################################################################################################

class QuickSort:
    '''
    Class containing methods to sort an array
    using quick-sort algorithm
    ...

    Attributes
    ----------
    '''

    def __init__(self):
        '''
        Function to intantiate a class object
        ...

        Parameters
        ----------
        None
        '''

        pass
    
    
    def find_midpoint(self, arr_length: int) -> int:
        '''
        Function to find middle index of an array
        ...

        Parameters
        ----------
        arr_length (int):
            length of the array

        Returns
        -------
        Middle index of the array
        '''

        midpoint = arr_length // 2

        return midpoint


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
        A partitioned list based on quick sort algorithm
        '''

        # Choose a random index from the array
        # and swap the first element of the array
        # with the element at the chosen index
        index = randint(l, r)
        arr[l], arr[index] = arr[index], arr[l]

        # Choose the first element of the array as pivot
        pivot = arr[l]

        # Initialise the indices
        i = l+1

        # Iterate through the elements of the array
        # swap the jth element with ith element if 
        # jth element is greater than the ith element
        for j in range(l+1, len(arr)-1):
            if arr[j] > p:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        
        # Swap first element array with element 
        # at (i-1)th element
        arr[l], arr[i-1] = arr[i-1], arr[l]

        return arr


    def qsort(self, arr: list) -> list:
        '''
        Function to sort array using quick sort
        ...

        Parameters
        ----------
        arr (list):
            array to be sorted

        Returns
        -------
        Sorted array
        '''

        # Base case, if length is 1 return the array
        if len(arr) <= 1:
            return arr

        # Find the middle index of the array
        m = self.find_midpoint(len(arr))

        # Break array into left and right halves
        l = 0
        r = len(arr)-1

        # Sorting the left and right half recursively
        self.partition(arr, l, m)
        self.partition(arr, m, r)

        return arr



