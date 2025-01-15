'''JSON is a data-interchange format derived from JavaScript. It is mostly used for storing or transferring data.
So, if we want our program to interact with the internet, we must be familiar with this module, even only to send or 
receive data through the internet. It is one of Python's most important modules because if we want it to interact only 
a bit through the internet, the Json module must be imported first. A JSON is an unordered collection of key and value 
pairs similar to a python dictionary. The following are some important points about JSON.


Keys are unique strings that cannot be null.

Values can be anything from a String, Number, Tuple, Boolean, list, or null.

A JSON is represented by a string which is enclosed within curly braces { } with key-value pairs which 
are separated by a colon ( : ), and pairs separated by a comma(, ).

Below is an example of JSON data. We can notice that the data representation is similar to Python dictionaries.'''
{"name": "harry", "salary": 9000, "language": "Python"}



# JSON in Python:

# JSON is already built-in in Python, so no need for an installation command. We can import it so we may start working on it. 
# JSON module in Python helps us in converting the data structures to JSON strings. Use the import function to import the JSON module in your Python program.


import json

# If we convert a JSON string to Python, the resultant will be a dictionary. The conversion is also known as parsing,
# and that is the keyword we use professionally for the conversion. We can convert from JSON to Python or Python to JSON by using json.loads() or json.dumps() methods. 

# Methods:

# load(): This method is used to load data from a JSON file into a python dictionary.

# Loads( ): This method is used to load data from a JSON variable into a python dictionary.

# dump(): This method is used to load data from the python dictionary to the JSON file.

# dumps(): This method is used to load data from the python dictionary to the JSON variable.

# Following is the program showing the use of JSON package in Python

import json
a ={"name":"harry","salary":9000,"language":"Python"}  

# # conversion to JSON done by dumps() function
b = json.dumps(a)
print(b) # printing the output

# Output:-
# {"name": "harry", "salary": 9000, "language": "Python"}


'''What parsing actually does?'''

'''Parsing converts the code from one form to another, making it compatible with running on the other platform by changing all the 
little syntax differences and making it perfect for running on the other platform. The following table shows how Python objects are converted to JSON objects.'''

# JSON	       PYTHON
# true     	   true
# false   	   false
# string       string
# number	   number
# array    	   list, tuple
# object 	   dict
# null         none



import json

data = '{"var1":"harry", "var2":56}'
print(data)

# print(data('var1'))        invalid

parsed = json.loads(data)
print((parsed('var1')))    # is valid

# printing parsed data and normal print data has differences , we can print var1 as parsed value in JS but not in python string print

parsed = json.loads(data)
print(type(parsed))
#class: dict

#Task 1 - json.load?


data2 = {
    "channel_name": "CodeWithHarry",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False
}

jscomp = json.dumps(data2)
print(jscomp)
# gives the ouput which is JS compatible ; like there False is 'false' .
# {"channel_name": "CodeWithHarry", "cars": ["bmw", "audi a8", "ferrari"], "fridge": ["roti", 540], "isbad": false}      [output]
# Task 2 = what is sort_keys parameter in dumps


'''JSON is most commonly used for client-server communication because it is human-readable and easy to read/write. JSON is mainly based on key-value pairs, 
similar to a dictionary in Python. To use the JSON module in Python, we have to import it. While using json.dumps(), we can send separators in parameters to 
make the code more readable and well defined. The separators could be full stops, commas, blank spaces, etc. '''

