"""

The following iterative sequence is defined for the set of positive integers:
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence: 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?

"""
# I will add all numbers and their sequence length to the all_sequences variable.
all_sequnces = dict()

# We can use different approaches to get result.
# But intutively we can easily get that the result should be higher than 500.000
# Becasue we have 2*x for each x less than 500.000 and sequence(2*x) is always
# longer than sequence(x) 
for i in range(5*10**5, 10**6):
    # To follow sequence use temp variable
    temp = i
    # To get sequence length use count
    count = 0
    # Sequence will go until we obtain 1 after operation given below.
    while temp != 1:
        # if temp is even now divide by 2 else multiply by 3 and add 1 
        temp = 3*temp+1 if(temp%2) else temp/2
        count += 1
    # Save to dictionary
    all_sequnces[i] = count

# get number that has longest sequence by sorting dict according to values
max(all_sequnces.items(), key=lambda x: x[1])