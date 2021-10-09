############################################ Script to implement merge sorting #########################################

'''
Python program to implement merge sort, the time complexity of the algorithms in nlogn.
'''

########################################################################################################################

class MergeSort:
    '''
    Class containing methods to implement merge sorting
    ...

    Attributes
    ----------
    None
    '''

    def __init__(self):
        '''
        Function to instantiate the class object
        ...

        Parameters
        ----------
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


    def merge(self, arr: list) -> list:
        '''
        Function to merge and sort two halves of
        array
        ...

        Parameters
        ----------
        arr (list):
            array of unsorted numbers
        
        Returns
        -------
        sorted array
        '''

        # Base case, when array has a length
        # of 1 or less
        if len(arr) <= 1:
            return arr

        # Recusrion to sort first and second
        # halves of array
        mid = self.find_midpoint(len(arr))      

        # Sorting left and right halves
        left = self.merge(arr[:mid])
        right = self.merge(arr[mid:])

        # Merging left and right halves
        i = 0
        j = 0
        temp = []

        while ((i < len(left)) or (j < len(right))):

            if i >= len(left):
                temp.append(right[j])
                j += 1
        
            elif j >= len(right):
                temp.append(left[i])
                i += 1

            elif left[i] <= right[j]:
                temp.append(left[i])
                i += 1
        
            elif left[i] > right[j]:
                temp.append(right[j])
                j += 1

            

        return temp



########################################################################################################################

if __name__ == '__main__':

    arr = list(map(int, input("Input numbers with space: ").split(" ")))

    merge_sort = MergeSort()

    result = merge_sort.merge(arr)

    print(result)