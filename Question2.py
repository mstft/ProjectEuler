# The sum of the even-valued Fibonacci terms which are less than 4 million.

# we set the limit which is 4 millon
limit = 4*10**6

# We know that the first term of the Fibonacci sequence is 0 and the second one is 1
# For more information visit: https://en.wikipedia.org/wiki/Fibonacci_number
term_1, term_2 = 0, 1

# sum of the terms will be added to the total variable 
total = 0

# continue to the process until term_1 reach the limit
while term_1 < limit:

    # According to the problem only even numbers in the sequence should be summed
    # I will make summation  in a more pythonic way

    # Explanation of line 21:
    #   Term 1 will be added total if it is an even number else it won't be added 
    total = total + term_1 if not (term_1 % 2) else total

    # we assign term_2 to term 1 and new term_2 will be (term_1 + term_2) 
    # in this way we will make progress 
    term_1, term_2 = term_2, term_1 + term_2

# print the total to find the anwser
print(total)
