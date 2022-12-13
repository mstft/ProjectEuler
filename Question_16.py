"""
What is the sum of the digits of the number 2**1000?
"""

# As python can easily calculate 1000th power of 2.
# We will get sum of the result of 2**1000

result = sum(int(i) for i in str(2**1000))
print(f"Answer for Question 16 is {result}")