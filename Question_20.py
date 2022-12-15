"""
Find the sum of the digits in the number 100!
"""

from math import factorial

# I will use factorial function from math lib to 
# calculate 100!
# Then use list comprehension to get sum of digits
result = sum(int(i) for i in str(factorial(100)))
# and print the result
print(f"Solution of the Question_20 is {result}")
