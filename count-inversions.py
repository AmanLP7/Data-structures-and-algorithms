####################################### Python script to count number of inversions ####################################

'''
Implementation of algorithm which count the numbers of inversions in an
array using divide and conquer paradigm.
'''

########################################################################################################################

class CountInversions:
    '''
    Class containing methods to count number of inversions
    ...

    Attributes
    ----------
    None
    '''

    def __init__(self):
        '''
        Function to instantiate the object of the class
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


    def merge_and_count_inversions(self, arr: list) -> list:
        '''
        Function to merge and sort two halves of
        array and count the number of inversions
        present
        ...

        Parameters
        ----------
        arr (list):
            array of unsorted numbers
        
        Returns
        -------
        Tuple containing sorted array as the first
        element and number of inversions as second
        '''

        # Base case, when array has a length
        # of 1 or less return tuple whose
        # first element is array and second 
        # element is number of inversions in it
        if len(arr) <= 1:
            return (arr, 0)

        # Recursion to sort first and second
        # halves of array
        mid = self.find_midpoint(len(arr))      

        # Sorting left and right halves
        left, left_inversions = self.merge_and_count_inversions(arr[:mid])
        right, right_inversions = self.merge_and_count_inversions(arr[mid:])

        # inversions in left and right halves
        inversions = left_inversions + right_inversions

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
                inversions += (len(left) - i)

            

        return (temp, inversions)



########################################################################################################################


if __name__ == '__main__':

    arr = list(map(int, input("Input numbers with space: ").split(" ")))

    count_inversions = CountInversions()

    result = count_inversions.merge_and_count_inversions(arr)

    print(result)

    