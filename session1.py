# Sarah Lohmeier, 2/22/16
# SESSION 1: Programming Basics

# In this workshop, we'll set up Cloud9 and write our first script in Python.
# Topics: executing scripts, intro to programming, comments, data types, logging, variables, functions, loops


# EXECUTING A SCRIPT

# A script is a name for a bit of code.
# To execute a script, make sure it's saved as "fileName.py" and hit the green run button at the top of the screen.

# Advanced: In the bash tab, next to the $, type:
#       python fileName.py


# WHAT IS PROGRAMMING?

# We make a list of commands for the computer to execute.
# The commands are given according to a list of rules defined by a language.
# The language we're using is called Python, and it's one of the easiest to use and understand.

# The computer reads through the file line-by-line and performs each command.
# If the computer doesn't understand a particular command because of a typo or other error,
# we won't get the results we want.


# COMMENTS

# Comments are sections of our file that we want the computer to ignore instead of executing as Python code.
# They're useful for making notes about what a particular chunk of codes does or who wrote it

# A hashtag is used to comment out a single line. Everything to the right of the hashtag will be ignored.

'''
Triple quotation marks are used to comment out multiple lines.
Anything within the quote marks will be ignored.
'''

# DATA TYPES

# Your computer wants to know what kind of input you're giving it.
# Python's smart enough to automatically assign the right data types to most input,
# but you need to be careful to format it correctly.

# We can store text as a data type called a string. Strings are always surrounded by quotation marks.
# They can be single or double quotation marks, as long as the start and end quotes are the same type.



'hello'
"i am the terminator"

# There are a couple different data types that handle numbers.
# The one you'll probably use the most is the integer, which includes zero and all whole negative and positive numbers.
# If the numbers are really extroardinarily large (think scientific notation),
# Python will use a different data type to store them, but integers will work fine for us here.

# Here's an example of an integer:
100

# Here's an example of a floating point-- Python's decimal.
0.5

# We can use square brackets and commas to make a list of items, called an array:
[0, 1, 2, 3]

# We can give true and false values, called Booleans. (Note the capital first letter and no quotation marks.)
True
False

# Python can handle lots of math for us:
100 + 1
100 / 50
2**3

# but how do we get it to tell us the answer?


# LOGGING

# If we want the computer to display something, one of the easiest ways to do that is to log something to the console.
# In Cloud9, the console is that tab that says "bash". On your own computer, you can use Terminal (if you're on a Mac)
# or PowerShell (if you're on Windows). Each will use slightly different commands to navigate through your files and 
# execute a Python script, but the Python commands stay the same no matter what operating system you're using.
# Consoles are nice when you want to execute commands very fast and without the bulk of an IDE, but they're not as
# user-friendly or forgiving as clicking around on icons and opening tabs and windows.

# Logging output to the console is a great way to show what your code is doing. It's also helpful if you're not sure
# where an error is in your code, and you need to track down what's going on.

# The 'print' command is used to log something to the console. 

#print 'Hello, world!'
#print 1337

# We can do commands within the print statement, and Python will just log the final output:

#print 2 + 2
#print 3 * (2 * 2)

# We can use the plus sign to put together strings, an action called 'concatenating':

#print 'my name is ' + 'sarah'

# By default, a print statement always ends on a new line.
# If we put a comma at the end of the print statement, it'll stay on that line and add a space:

#print 'so we can go on', 'and on', 'and on!',

# If we don't specify what to log, it'll just give us a blank line:
#print "first line"
#print
#print "next line"


# VARIABLES

# We can store values by creating variables and assigning values to variables.

example_variable = 3

# Now the example variable has been assigned a value of 3.
# The computer will automatically substitute in the current value any time we use the variable:

#print example_variable

#second_example_variable = example_variable + 1
#print second_example_variable
#print second_example_variable + 100

# The variable is just a container for a value, so we can change the value of the variable as often as we like.

example_variable = "cat"

example_variable = True


# FUNCTIONS

# If we want to run the same set of commands over and over, we can combine the commands into a function.
# A function is a series of transformations that turn an input into an output.
# A function is created by using the command 'def', giving the name of the function you're making,
# and then putting the names of whatever variables you want to use as input in parentheses.


# We can give strings, numbers, or Booleans as input,
# or we can just do empty parentheses if the function doesn't need any input.
# Python uses whitespace to indicate where the function's set of commands begins and ends.


def printFunction(s):
    x = "hello "
    z = x + s # the plus sign concatenates two strings
    print z


# remove the pound sign in the next line to run this function on the input string 'programmers!'

name = 'Sarah'


#printFunction(name)

def greet():
    print "greetings!"




# we can also ask a function to return an output instead of just printing it out,
# so we can store it as a value or use it in another function.


def sum(n1, n2):
    return (n1 + n2)
 
 
x = sum(1,2)
#print x


# this does the same thing as print sum(1,2)


# LOOPS

# If we want the computer to do something for a certain period of time, we can use a loop.
# In python, two of the most common loops are for-loops and while loops.



def printDigits(x):
    i = 0
    while i < x:
        print i
        i = i + 1

#printDigits(3)


# range(x) is the same as an array of the first ten digits: [0,1,2,3,4,5,6,7,8,9]

result = []

for x in range(10):
    result.append(x)

#print result

# if we want the computer to only do something under certain conditions, we can use an if/then conditional statement:

if 8 / 2 == 0:
    print "8 is an even number"
elif 8 % 2 == 1:
    print "8 is an odd number"
else:
    print "something weird must be happening!"

    

#print

# this just skips a line when we print to the console in the tab below.


# now we can try putting all of these things together into functions!


# what if we want to print a triangle?


def triangle(x):
    i = 1
    while i <= x:
        print i * "0"
        i = i + 1

#triangle(3)


# see what other shapes you can make!

