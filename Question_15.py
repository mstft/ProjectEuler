"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""

# In total we should take 40 steps 20 of them will be on right & the rest 20 will be downward.
# This means we can get solution to combination of (40, 20)

# for this we can use factorial from math lib.
from math import factorial

print(f"Result of Question 15 is {factorial(40)/(factorial(20)**2)}")