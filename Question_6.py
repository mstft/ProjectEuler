"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

# It is (1+2+...+100)**2-(1**2+2**2+...+100**2)
# we know that the first term (sum of consecutive numbers from 1 to n) is n*(n+1)/2
n = 100
first_term = (n * (n + 1) / 2)**2

# Second term is sum of squares of consecutive numbers which can be formulated as
# n*(n+1)*(2*n+1)/6
# https://www.cuemath.com/algebra/sum-of-squares/ 
second_term = n * (n + 1) * (2 * n + 1) / 6

result = first_term - second_term
print(result)