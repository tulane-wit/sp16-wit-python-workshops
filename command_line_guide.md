# Guide to running Python through the command line


### For Mac users:


1. Make a dedicated folder for all your code snippets (for now, we’ll call it pyFiles) on your Desktop.


2. Download the TextWrangler text editor (http://www.barebones.com/products/textwrangler/), install it, and open a new file.


3. In your TextWrangler file, type the following:

	print “hello world”


4. Save the file as helloWorld.py and save it inside the pyFiles folder you made earlier.


5. Go to Launchpad and open up the “Terminal” application. If you wait a second, a window will pop up with a little prompt that should look something like:

	Sarahs-MacBook-Pro:~sarahlohmeier$

You’re now working in your computer’s command line. The bit to the left of the colon (“Sarahs-MacBook-Pro”) is the name of your computer. The bit to the right of the colon shows what folder the Terminal is looking at currently— by default, it’s in your home folder (“sarahlohmeier”, for me). The tilde (~) just means that the folder you’re currently working in is within another folder. The dollar sign ($) means that the command line is ready to accept a command.


6. Inside the window, next to the prompt,  type the following:

	python /Users/sarahlohmeier/Desktop/pyFiles/helloWorld.py

and hit enter. (replace “sarahlohmeier” with whatever your home folder name is— it’ll be whatever’s between the ~ and the $ in the prompt.


7. If everything works correctly, the computer should execute the helloWorld.py program and print:

	hello world

to the Terminal directly below the command you entered. A new prompt should then appear on the line below, indicating that the command was successfully executed and the computer’s ready for a new command.







## For Windows users:



1. Download python (version 2.7, NOT 3!) from https://www.python.org/downloads/ and install it.


2. Open a command prompt window by going to Start > All Programs > Accessories > Command Prompt. A window will appear with a prompt that looks something like:

	C:\Users\MyName>

You’re now working in your computer’s command line. The bit to the left of the greater-than sign (>) is the folder in the computer where you’re currently working— this should be your user folder by default. The > is just a little pointer indicating that your computer is ready to execute whatever command you type to the right of the > sign.


3. Inside the window, next to the prompt, type:

	python

and hit enter. If you see something like: 

	Python 2.7.9 (default, Apr 16 2015, 13.37:22) [MSC v.1500 32 bit (Intel)] on win32
	Type “help”, “copyright”, “credits” or “license” for more information.
	>>>

then Python’s all ready to go and you can move on to step 4 now.


3b. If instead you got:
	‘python’ is not recognized as an internal or external command, operable program or batch file.

or:
	Bad command or filename

Then you need to show your computer where to find the Python program files you just installed. There’s a good walkthrough of this process here:

http://www.pythoncentral.io/add-python-to-path-python-is-not-recognized-as-an-internal-or-external-command/


4. Once you get all that working, type next to the >>>:

	quit()

and hit enter.


5. Make a dedicated folder for all your code snippets (for now, we’ll call it pyFiles) on your Desktop.


6. Download the Notepad++ text editor (http://notepad-plus-plus.org/), install it, and open a new file.


7. In your Notepad++ file, type the following:

	print “hello world”


8. Save the file as helloWorld.py and save it inside the pyFiles folder you made earlier.


9. Go back to the Command Line window and, next to the prompt, type:

	python C:\Users\MyName\Desktop\pyFiles\helloWorld.py

and hit enter. (Replace ‘MyName’ with the name of your home file— this should be whatever’s in between “Users\” and “>” in the prompt.)

7. If everything works correctly, the computer should execute the helloWorld.py program and print:

	hello world

to the Command Line window directly below the command you entered. A new prompt should then appear on the line below, indicating that the command was successfully executed and the computer’s ready for a new command.
