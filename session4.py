'''
Sarah Lohmeier, 3/13/16
SESSION 4: Web Scraping

In this workshop, we'll explore automating data retrieval from the web via web scraping.

Topics: web page structure, web scraping, web servers, html, urllib2

LINKS:
https://docs.python.org/2/library/urllib2.html
http://www.w3schools.com/
https://docs.python.org/2/tutorial/inputoutput.html

'''

import urllib2

site = urllib2.urlopen('https://hollygrovemarket.com/whats-in-the-box/')

siteText = site.read()

file1 = open("data.txt", "a")


file1.write(siteText)
file1.close



file2 = open("data.txt", "r")

for i in range(2300):
    current_line = file2.readline()
    j = 0
    while (j+6) < current_line.length:
        if current_line[j:j+6] == "<head>":
            print "found the head tag!"
        j = j+1
        



'''

date = file2.readline() # extract the line containing the date.
date = date[14:]

print date'''