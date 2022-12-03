"""
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a**2 + b**2 = c**2

    For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
"""

# We should find a, b and c. As it's asked for numbers smaller than 1000 it's ok to run a loop
# From the equation we can write c = sqrt(a**2+b**2)
# Another condition that should be satisfied is a+b+c==1000 => a+b+(a**2+b**2)**0.5==1000
result = [a*b*(a**2 + b**2)**0.5 for a in range(1, 998) for b in range(a,1000) if (a**2 + b**2)**0.5+a+b==1000]

# As there exists exactly one a,b,c satisfies these conditions we can get first and the only 
# element of the result
print(result[0])