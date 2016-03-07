'''
Sarah Lohmeier, 3/7/16
SESSION 3: Graphics and Animation

2D ARRAYS
'''

# helper function
def matrix_print(matrix):
    print '['
    for i in range(len(matrix)):
        line = '['
        for j in range(len(matrix[i])):
            line = line + str(matrix[i][j]) + ', '
        line += '],'
        print line
    print ']'


# A regular array holds a single line of information:

array = [0, 0, 0, 0,]

# Which is a problem if we want to store a grid.
# We can solve this by storing arrays inside arrays-- essentially creating a matrix:

example_matrix = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

#matrix_print(example_matrix)

# We can access an entire row in a matrix:

#print example_matrix[0]
example_matrix[0] = [2, 0, 0, 0]
#matrix_print(example_matrix)

# We can also access single elements by specifying what row and column they're in:

example_matrix[1][2] = 4

matrix_print(example_matrix)

# This is the basis for manipulating pixels on a screen.

# With the right GUI (http://www.codeskulptor.org/#poc_2048_gui.py), it's also the basis for 2048!

# http://www.codeskulptor.org/#user34_cHRBjzx8rx_114.py
