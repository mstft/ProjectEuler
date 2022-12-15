"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below ...
Find the maximum total from top to bottom of the triangle below.
"""

# read the file and split according to lines
lines = open('Question_67.txt').read().split('\n')

# convert to a matrix in list
tree = [[int(i) for i in a.split(' ')] for a in lines]

# search through tree from bottom to top
for i in range(len(tree)-1,0,-1):
    t = tree[i]
    # add each sum to 
    for j in range(0,len(t)-1):
        # choose max of two possible path to upward
        a = max(t[j],t[j+1])
        # add it to element at higher level
        tree[i-1][j] += a
# First element is the maxsimum total  
print(tree[0])