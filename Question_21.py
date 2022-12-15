"""

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.


"""
# numbers under 10000 will be checked
last_number = 10000
total = 0

# control each number
for i in range(1, last_number):
    # find sum of all divisors less than number a result will be b
    first = sum(j for j in range(1, i) if i%j==0)
    # find sum of divisors of number b (found above) result should be a to make case True
    second = sum(j for j in range(1, first) if first%j==0)
    # div(b) which is second should be a & a and b should not be same 
    if (second == i) and (first != second):
        total += i
print(total)