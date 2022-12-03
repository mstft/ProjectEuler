import numpy as np

"""
What is the 10.001st prime number?
"""

# As we can do math operation on numpy arrays
# wrt to sets and lists we add numpy lib.

# it is asked for 10001st prime. 
# Set it as limit
limit = 10001

# add first prime number to prime list
prime_list = np.array([2]) 

# pointer is the number we check whether is prime or not
pointer = 3

# we will continue the operation until we found 10.001st prime
# it means when len of prime list reached 10.001 it will stop the loop
while prime_list.size < limit:
    # if pointer is a prime number pointer%each_number_in_prime_list 
    # will be non zero and it means np.all(...) will be True
    if np.all(pointer%prime_list):
        # if it's True pointer is prime then add to prime_list
        prime_list = np.append(prime_list, pointer)
    # check next odd number's prime stiuation 
    pointer += 2

# prime_list now contains 10.001 prime number.
# just get the last added one, or max of prime_list
print(prime_list[-1])