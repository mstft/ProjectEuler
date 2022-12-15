"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below ...
Find the maximum total from top to bottom of the triangle below.
"""



lines = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

# convert a list and remove spaces begining and
# end of lines 
matrix = lines.strip().split('\n')
# convert to a matrix in list
tree = [[int(i) for i in a.split(' ')] for a in matrix]

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