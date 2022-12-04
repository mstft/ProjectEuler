import numpy as np

"""
    Find the sum of all the primes below two million.
"""

# It's asked to check for primes below 2 million. 
# Therefore we set limit to 2 million
last = 2*10**6

# We will use a true false array to represent prime numbers.
# If index of element is prime then element will be True else False.  
tf_array = np.array([False]*2+[True]*last)
# For index 0 and 1 related elements are false as 0 & 1 are not prime.
# For the rest we will check with for loop given below

# Here we will use Sieve of Eratosthenes method
# For details https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes 
# If x is a prime number, then all multiples of x (2*x,3,*x...) are non-prime
# We will use numpy to assign False to all multplies(2*x-...) of X
# As they are non prime 
for i in range(0, tf_array.size):
    # if tf_array is True
    if tf_array[i]:
        # set multiples of i to False
        tf_array[2*i::i] = False
        
# Numbers from zero to 2000001
# 2 million or 2 million+1 won't change anything
prime_finder = np.arange(last+2)

# As tf_array is True only if index of element is prime
# prime_finder[tf_array] equation will get prime numbers
# Finally we can use sum() to get sum of all primes in prime_finder
print(sum(prime_finder[tf_array]))