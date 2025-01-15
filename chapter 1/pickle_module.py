'''Pickle means to preserve, and in Python, we use it for the same purpose. Pickle comes in handy while saving complicated data. 
They are easy to use, lighter, and do not require several lines of code. The pickled file generated is not easily readable and thus 
provides some level of security.'''


'''Pickling is the process of serializing an object. Serializing means storing the object in the form of binary representation so it can be
saved in our main memory. The object could be of any type. It could be a string, tuple, or any other sort of object that Python supports. 
The data is stored in the main memory in a file. While writing the code for pickling, we open the file in "wb" mode, also known as writing binary mode. 
So, to use the pickle module, we have to make a file with the .pkl extension and send it in a dump() function along with the object. 
dump() is a built-in function in the Pickle module, made for pickling.'''



import pickle

# Pickling a python object
# cars = ["Audi", "BMW", "Maruti Suzuki", "Harryti Tuzuki"]
# file = "mycar.pkl"
# fileobj = open(file, 'wb')                    list object
# pickle.dump(cars, fileobj)
# fileobj.close()


# py_dict = { 'name': 'harry', 'salary':9000, 'language': 'Hindi' }
# myfile = open('filename','wb')
# pickle.dump(py_dict,myfile)                 dict object
# myfile.close()


'''The file format is binary, so we cannot directly open and read it; instead, we have to open it using a  python program, and the process 
is known as unpickling. We have to open the file in "rb" mode for unpickling, also known as a read binary mode. The function we use this time 
is also a built-in function, named load(). Unlike dump(), we have to send the file name as a parameter, and it automatically retrieves the data 
in the object type it was inserted in. For example, if we send a list while pickling, the return result will also be a list.'''

file = "mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))

'''To make sure that you successfully unpickled it, you can print the dictionary, compare it to the previous dictionary and check its type with type().d")
We can face some of the common pickle exceptions raised while dealing with the pickle module.

Pickle.PicklingError: If the pickle object does not support pickling, then Pickle.PicklingError exception is raised.

Pickle.UnpicklingError: This exception will raise if the file contains bad or corrupted data.

EOF Error: This exception will be raised if the end of the file is detected.'''

# pickle.load() - takes file object and return corresponding python format (readable ) 
# pickle.loads() - takes the binary format and returns python format
# pickle.dumps() - takes the variable and returns binary string

'''Disadvantages:

There are some situations in which pickling is discouraged. For example, when we are working with multiple  programming languages, pickle is discouraged.
Pickle has been found slower than its alternatives.
In some cases, it has also shown a few security vulnerabilities.
When we update our program to a newer version, pickled data through the previous version can cause issues.
When you need a cross-language solution, JSON is a better option.'''




# pickle
# Use requests module to download the iris dataset

import requests
import pickle

data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
# print(data)

# l1 = data.split("\n")
# print(l1)         
# new line character se split and convert it into list


l2 =[item.split(",") for item in data.split("\n") if len(item)!=0]    # used list comprehension
# print(l2)           a list of lists


with open("myiris.pkl", "wb") as f:           # open file in binary mode to pickle file or l2
    pickle.dump(l2, f)


# To read this pickle file you can use this code
# import pickle
# with open("myiris.pkl", "rb") as f:
#     print(pickle.load(f))
