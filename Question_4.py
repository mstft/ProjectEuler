# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

palindromes = set()

# It's asked for biggest number. 
# Therefore we can start from highest 3 digit number to lowest 3 digit number.
for first in range(999, 100, -1):
    # we will choose second number range(1, first)
    # but again we will start to multiply with big ones firstly
    for second in range(first, 100, -1):
        # as we will check palindrome case we convert multiplication to string
        num_str = str(first * second)
        # if str == str.reversed() it means it is a palindrome. To check this;
        if num_str == num_str[::-1]:
            # if it is then add to our set
            palindromes.add(num_str)
            # we can have other palindrome for other second values
            # but it will be smaller than the one we just added set
            # therefore we just break for second loop
            break
# to print highest palindrome number we can use max() method
# but as we add string we can control key parameter with lambda
# or just change line 18 as 
# palindromes.add(int(num_str)) and use print(max(palindromes))
print(max(palindromes, key=lambda x: int(x)))