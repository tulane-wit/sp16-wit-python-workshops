'''
Sarah Lohmeier, 4/4/16
SESSION 5: API's

In this workshop, we'll introduce what API's are and how to use them.

Topics: API's, HTTP RESTful principles, JSON, endpoints, fields

**** go ahead and sign up for an API Key: http://sunlightfoundation.com/api/accounts/register/

LINKS:
https://docs.python.org/2/library/urllib2.html
http://sunlightfoundation.com/api/


API's

API stands for Application Programming Interface.

It's a standardized way to send and retrieve data from an application.
Applications make their own API's, where they define the rules for accessing their data.

We can use any language we like to create the data requests (we'll keep using Python),
as long as the request is formatted correctly, according to their rules.

Every API will have its own documentation- a quick Google search will usually turn it up.

Here's an example of an API call, courtesy of Codecademy:
'''


from urllib2 import Request, urlopen, URLError

kitten_request = Request('http://placekitten.com/')

try:
	kitten_response = urlopen(kitten_request)
	kittens = kitten_response.read()
	print kittens[559:1000]
except URLError, e:
    print 'Failed. Error code:', e
    
'''
HTTP

HTTP, HyperText Transfer Protocol, is the protocol your browser uses to send and recieve
webpage information. Urllib2 uses HTTP to submit and fetch data from a url.

If the HTTP request fails for some reason, the request will return an error code:
https://http.cat/


REST

is guided by a set of principles called REST: Representational State Transfer.

Many APIs also use RESTful architecture. This means that you will only ever use four different
types of requests: GET, PUT, POST, and DELETE.

1. GET: retreives data
2. PUT: updates/replaces data
3. POST: creates data
4. DELETE: removes data

The API we'll be working with today is called OpenStates:
http://tryit.sunlightfoundation.com/openstates
'''

# be sure you have the full url, including the 'http://' part!
legislator_request = Request('http://openstates.org/api/v1//legislators/?state=la&active=true&apikey=6c25fff7e6e943f1891565b1ff7a967c')

try:
	legislator_response = urlopen(legislator_request)
	legislators = legislator_response.read()
	print legislators[0:100]
except URLError, e:
    print 'Failed. Error code:', e

'''
JSON

Notice the way the results are formatted-- see all the brackets and quotes?
That's called JSON (JavaScript Object Notation). It's not a programming language,
it's just a standardized way to structure any kind of data.

Check out W3's JSON guide for examples and more info:
http://www.w3schools.com/json/

The API documentation will describe the format of the results. With that, we can go through
the result data and parse it just like we did with the html page in session 4!
'''
