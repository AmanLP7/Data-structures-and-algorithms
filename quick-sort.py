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


    def qsort(self, arr: list, l: int, r: int) -> list:
        '''
        Function to sort array using quick sort
        ...

        Parameters
        ----------
        arr (list):
            array to be sorted
        l (int):
            left most index of the array
        r (int):
            right most index of the array

        Returns
        -------
        Sorted array
        '''

        # Base case, if left index is greater
        # than or equal to righ index then
        # return array
        if l >= r:
            return arr

        # Partitioning the array 
        a, l, p, r = self.partition(arr, l, r)
        
        # Partitioning left portion of pivot
        self.qsort(arr, l, p)

        # Partitioning right portion of pivot
        self.qsort(arr, p+1, r)

        return arr



#######################################################################################################################

if __name__ == '__main__':

    arr = list(map(int, input("Input the numbers: ").split(",")))

    qs = QuickSort()

    print(qs.qsort(arr, 0, len(arr)))



