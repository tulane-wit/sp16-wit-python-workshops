'''
Sarah Lohmeier, 3/7/16
SESSION 3: Graphics and Animation

TURTLE LIBRARY

The Python turtle library is a simple tool for drawing on a screen.

Cloud9 does NOT currently support the turtle library. You'll need to run it from your computer's command line.
Read command_line_guide.md for how to get started using your command line.

documentation: http://www.eg.bucknell.edu/~hyde/Python3/TurtleDirections.html
'''

from turtle import *

canvas = Screen()

tina = Turtle()

#tina.forward(100)

# We can use the forward(), backward(), left(), and right() commands to define fuctions that draw out shapes:

def square():
	for i in range(4):
		tina.forward(100)
		tina.right(90)

square()

# We can use arrays to provide input:

tina.pensize(10)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
for c in colors:
	tina.pencolor(c)
	square()


canvas.exitonclick() 