# What is the largest prime factor of the number 600851475143?
# more about prime numbers: https://en.wikipedia.org/wiki/Prime_number 

num = 600851475143

# it's only asked for just one number (which is assigned to num variable)
# therefore we can divide num to it's small prime factors to find all it's
# prime factors and later we can choose max of them

# num is an odd number therefore we can start to check prime factors from 3
# and add +2 in each time
start = 3
for i in range(start, int(num**0.5) + 1, 2):
    # if num is divisible by i number num%i will be 0 and (not 0) is True.
    if not num%i:
        # to remove multiples of i (if there is) from num
        while not (num%i):
            # now divide num to prime factor i. To go for the next prime factor. 
            num //= i
        # num is 1 means finally we reach num's largest prime factor. 
        # Just print it
        if num == 1: print(i)