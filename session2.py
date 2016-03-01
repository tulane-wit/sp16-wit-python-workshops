'''
Sarah Lohmeier, 2/29/16
SESSION 2: Choose-Your-Own-Adventure Games

In this workshop, we'll use the tools from Session 1 to make a choose-your-own adventure game.
Topics: input, type conversion, possibly arrays

'''

# INPUT

# The same way that we can use the print command to send data to the terminal, Python also has a command to accept
# user input from the terminal.

#raw_input()
#raw_input("Batman vs Superman: who wins? ")

# The response is stored as a string exactly as you typed it, including spaces, capitalization, and punctuation.

# We can store these user responses as variables:

#favorite_avenger = raw_input("Who's your favorite Avenger?")

# And from there, we can use loops, conditionals, and functions to create whatever we want.
'''
if favorite_avenger == 'Black Widow' or favorite_avenger == 'black widow':
    print "That's my favorite, too!"
elif favorite_avenger == 'Cap':
    print "GO USA"
'''
    
# Python stores all raw_input() as strings. So if we want Python to treat it as a number, we have to explicitly
# convert the data type Python is using for a value.
'''
x = "3"
print type(x)
x = int(x)
print type(x)
'''

# This works exactly the same for str(), float(), and bool().

'''
CREATING A CHOOSE YOUR OWN ADVENTURE GAME

Example: http://aliendovecote.com/uploads/twine/kesha.html

Let's make our own game that's played in the terminal!

1. Welcome the player
2. Prompt the player for a name and store it
3. Introduce a choice and prompt the player to make a choice
4. Describe a change in the story based on the choice.

Repeat steps 3 - 4 as many times as you want!

Some possible ideas:
- an "escape the room" style game
- a combat based game
- a quest-based game

'''

print "Welcome to the game!"
username = raw_input("What's your name, player?")
print "Hello", username, "!"