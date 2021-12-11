########################################## Python script to find ith smallest element ##################################

'''
Python script to find ith smallest element in an array. Time complexity is O(n).
'''

########################################################################################################################

### Importing required modules

# System library imports
from random import randint          # To chose a random element in a given range


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


    def partition(self, arr: list, p: int) -> list:
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
        p (int):

        Returns
        -------
        A tuple containing:
        1. Partitioned array
        2. Position of pivot element
        '''

        # Swap the first element of the array
        # with the element at the given index p
        arr[0], arr[p] = arr[p], arr[0]

        # Choose the first element of the array as pivot
        pivot = arr[0]
 
        # Initialise the indices
        i = 1

        # Iterate through the elements of the array
        # swap the jth element with ith element if 
        # jth element is smaller than or equal
        # to the pivot element
        for j in range(1, len(arr)):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        
        # Swap first element of array 
        # with element at (i-1)th index
        arr[0], arr[i-1] = arr[i-1], arr[0]

        return (arr, i-1)


    def random_select(self, arr: list, element: int) -> int:
        '''
        Function to recursively select ith element
        ...

        Parameters
        ----------
        arr (list):
            list to select elements from
        element (int):
            position of element

        Returns
        -------
        ith element from the array
        ''' 

        # Length of the array
        arr_len = len(arr)

        # Base case, when array contains only one element
        if arr_len <= 1:
            return arr[0]

        # Choose an index from array at random
        p = randint(0, arr_len-1)

        # Partition the array around element at p
        # and get element at new partition index
        arr, statistic = self.partition(arr, p)

        # If returned statistic equals the required statistic 
        # return the element at the index, if returned statistic
        # is greater recursively search for the statistic in the 
        # first half of the array less than statistic, else
        # recursively search for the statistic in the second half 
        # of the array greater than statistic
        if statistic == element-1:
            return arr[statistic]
        elif statistic > element-1:
            return self.random_select(arr[:statistic], element)
        elif statistic < element-1:
            return self.random_select(arr[statistic + 1:], element-1-statistic)

    

########################################################################################################################


if __name__ == '__main__':

    arr = list(map(int, input("Please enter the list seperated by space: ").split(" ")))

    fe = FindElement()

    order = int(input("\nPlease enter the order of the statistic you want to find: "))

    result = fe.random_select(arr, order)

    print(f"\nThe order {order} statistic is = {result}\n")
