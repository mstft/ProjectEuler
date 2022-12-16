"""
Using a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
# Instead of writing all uppercase letters we can use string ascii_uppercase
from string import ascii_uppercase

# open file and save to variable mt
with  open('Question_22.txt') as file:
    mt = file.read().split(',')
    
# as the question is asking to sort words 
mt = sorted(mt)

# total score is the result
total_score = 0

# go through list with enumerate to get place of word and word itself 
for place, word in enumerate(mt):
    name_score = 0
    # we have "" from begining and end of each number to remove them use [1:-1]
    for letter in word[1:-1]:
        # get index from ascii_uppercase and add 1 as index is -1 of the place in word
        name_score += (ascii_uppercase.index(letter) + 1)
    # multiply name score and place of word and add to total score
    total_score += (name_score * (place + 1))

print(f"Answer of Question 22 is: {total_score}")