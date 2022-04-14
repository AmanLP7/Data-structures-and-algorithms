##################################################### Sieve Of Eratosthenes ############################################

'''
Algorithm to find prime number less than a given number n. The time complexity of this
algorithm is O(nloglogn).
'''

########################################################################################################################


class FindPrimes:
    ''' 
    Class containing modules to find prime numbers upto a number n
    ...

    Attributes
    ----------
    None
    '''

    def __init__(self):
        ''' 
        Function to instantiate class object.
        ...

        Parameters
        ----------
        None
        '''
        pass


    def find_prime_less_than(self, n: int) -> list:
        '''
        Function to find prime numbers less than 
        a given number n.
        ...

        Parameters
        ----------
        n (int): Upper limit

        Returns
        -------
        A list of numbers less than n which are prime
        '''

        primes = [True]*(n+1)
        
        for i in range(2, int(n**(1/2)+1)):
            if primes[i]:
                for j in range(i**2, n+1, i):
                    primes[j] = False

        numbers = []
        for i in range(2, len(primes)):
            if primes[i]:
                numbers.append(i)

        return numbers


########################################################################################################################

if __name__ == "__main__":

    P = FindPrimes()
    result = P.find_prime_less_than(20)

    print(result)

