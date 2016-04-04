'''
Sarah Lohmeier, 3/7/16
SESSION 3: Graphics and Animation

1D ARRAYS
'''

# Arrays are ordered collections of elements:

example_array  = ['a', 'b', 'c']

# They can be any size and can contain any data type(s) -- or can contain nothing!

# You can use the len() command to figure out the length of the array:

#print len(example_array)

# Arrays always have the same index values, starting at 0.



# MANIPULATING ARRAY ELEMENTS

# Elements in an array are accessed with the name of the array and the index:

#first_letter = example_array[0]



# Elements are easily added onto the end:

example_array.append('d')


# And you can slice arrays to select a subset of the array elements.
# The start index value is inclusive, the end index value is exclusive.

example_array = example_array[0:3]



# ITERATING OVER ARRAYS

# You can use loops to access each element in an array in order.

# One option: set the index variable to 0....n

index_array = []
for i in range(len(example_array)):
    index_array.append(example_array[i])
    

#print index_array

# Another option: set i equal to each element, with a nifty Python shortcut.

result_array = []
for i in example_array:
    result_array.append(i)

print result_array

# check out the official Python array documentation for the whole list of built-in array functions:
# https://docs.python.org/2/library/array.html