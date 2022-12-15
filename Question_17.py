""" 
Question 17:
    If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
"""

# We will use dictionary to solve the problem.
# But as it is asked to get number of letters will be used we will just write 
# the number of letters will be used. For this case we will write the case
# where if the two last digits of number is between 10-20
# Because 41 is written as fourty + one but 11 is not written as ten one 
# the whole word. e.g. instead of 1:'one' write 1:3 => as len('one') is 3
eleven_twenty_conversion = {11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}

# for other numbers last digit conversion
last_digit_conversion = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4}

# for numbers in range(10,90,10) we can write as
second_digit_conversion = {0:0, 1:3, 2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}
# for hundreds we will just add hundred to end of number therefore
# we can use last_digit_conversion and add len("hundred") to letter_used
letters_used = 0
# limit is
last_number = 1000

for number in range(last_number):
    # reverse number to handle positions easily
    for position, digit in enumerate(str(number)[::-1]):
        if position == 0:
            # add length of smallest digit
            letters_used += last_digit_conversion[int(digit)]
        elif position == 1:
            # if last two digit of the number is in range 11-20
            # it will be written as in eleven_twenty_conversion
            # use that conversion and remove added length for 
            # position 0 
            if 10<number%100<20:
                letters_used += eleven_twenty_conversion[number%100]
                letters_used -= last_digit_conversion[number%10]
            # else then use normal conversion
            else:
                letters_used += second_digit_conversion[int(digit)]
        elif position == 2:
            # add len(digit_in_word) + hundred
            letters_used += (last_digit_conversion[int(digit)] + len("hundred"))
            # add and between numbers e.g. one hundred AND four
            if number%100!=0:
                letters_used += 3
        else:
            print("You are not in the limits!!!")
# our last number is 1000. Then length of it to letters_used
letters_used += len("onethousand")            
print(letters_used)