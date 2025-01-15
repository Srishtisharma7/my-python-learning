'''The Python Requests module is an HTTP library that enables developers to send HTTP requests in Python. This module enables you to send 
HTTP requests using Python code and makes it possible to interact with APIs and web services.'''

import requests

# example that sends a GET request to the Google homepage:
response = requests.get("https://www.google.com")
print(response.text)


# Here is another example that sends a POST request to a web service and includes a custom header:
# In this example, we send a POST request to a web service to authenticate a user. 
# We include a custom User-Agent header and a JSON payload with the user's credentials.

import requests

url = "https://api.example.com/login"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Content-Type": "application/json"
}
data = {
    "username": "myusername",
    "password": "mypassword"
}

response = requests.post(url, headers=headers, json=data)

print(response.text)

# data = {
#     "title": 'harry',
#     "body": 'bhai',
#     "userId": 12,
#   }
# headers =  {
#     'Content-type': 'application/json; charset=UTF-8',
#   }
# response = requests.post(url, headers=headers, json=data)

# print(response.text)


#example:

import requests 
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
r = requests.get(url)
# print(r.text)


soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
for heading in soup.find_all("h2"):
  print(heading.text)
# url = "https://jsonplaceholder.typicode.com/posts"



# get():
# From the name, we can detect that the get function returns us some information about the site we requested. All the information 
# is stored in the object we used to send the request. We can access different kinds of information through it, such as status, header, 
# cookies, etc. To make a GET request, invoke

# The basic syntax is:
# requests.get(URL, params={key: value}, args)


# URL: this is the URL of the website where we want to send the request. 
# Params: this is a dictionary or a list of tuples used to send a query string. 
# Args: It is optional. It can be any named arguments offered by the get method.
# We can also fetch all the data from the homepage of a website into an HTML format using the request module. 



# Few important types of methods defined:


'''put( ):
 It is used to send a put request to a variable. It is usually used to update or completely change the resources of a specific URL.
 
delete( ):
Delete is used to delete the specific resource specified by URL.
 
head( ):
The head method returns a header for a specific resource.

post( ):
Post requests take with it the data to the server to update it with.

patch( ):
The patch is used to send patch requests. It is used to apply partial modifications to a resource. It carries with it the instructions for the modification.
For more detail, you can check the Python documentation about the requests module. This tutorial ends here, and I will see you in the next tutorial.'''