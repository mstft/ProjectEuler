import math
from functools import reduce

""" Question  5: 
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? """

# Approach: first we will find prime numbers in range(1, 20)
limit = 20
# And later we will find maksimum power of each prime which is also less than limit
# As for e.g. if a number is divisible with 3 and 5 it is also divisible with 3*5

# First prime is 2
# We can write other primes that are smaller than 20 or just run code between lines 11-14
primes = {2}

# To obtain other primes we check odd numbers between 3-20
for i in range(3, 20, 2):
    # If a number has remainder when it is divided to all primes less than it 
    # Then it is a prime number. all() returns True if this condition is satisfied; 
    if all(i%j for j in primes):
        primes.add(i)

# Now we can find with log function how many times we need each prime and we can multiply them
# For this we add math lib and to multiply on a single line we import "reduce" method from functools
result = reduce(lambda x,y: x*y, [prime**int(math.log(limit, prime)) for prime in primes])
print(result)