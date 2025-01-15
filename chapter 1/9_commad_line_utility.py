'''Command line utilities are programs that can be run from the terminal or command line interface, and they are an essential part of 
many development workflows. In Python, you can create your own command line utilities using the built-in argparse module.'''

import argparse

parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument("arg1", help="description of argument 1")
parser.add_argument("arg2", help="description of argument 2")

# Parse the arguments
args = parser.parse_args()

# Use the arguments in your code
print(args.arg1)
print(args.arg2)


import argparse
import requests

def download_file(url, local_filename): 
  if local_filename is None:
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
  with requests.get(url, stream=True) as r:
      r.raise_for_status()
      with open(local_filename, 'wb') as f:
          for chunk in r.iter_content(chunk_size=8192): 
              # If you have chunk encoded response uncomment if
              # and set chunk_size parameter to None.
              #if chunk: 
              f.write(chunk)
  return local_filename
  
parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument("url", help="Url of the file to download")
# parser.add_argument("output", help="by which name do you want to save your file")
parser.add_argument("-o", "--output", type=str, help="Name of the file", default=None)

# Parse the arguments
args = parser.parse_args()

# Use the arguments in your code
print(args.url)
print(args.output, type(args.output))
download_file(args.url, args.output)


# Here are a few examples to help you get started with creating command line utilities in Python:



# Adding optional arguments
# The following example shows how to add an optional argument to your command line utility:

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--optional", help="description of optional argument", default="default_value")
args = parser.parse_args()

print(args.optional)




# Adding positional arguments
# The following example shows how to add a positional argument to your command line utility:

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("positional", help="description of positional argument")
args = parser.parse_args()

print(args.positional)




# Adding arguments with type
# The following example shows how to add an argument with a specified type:

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, help="description of integer argument")
args = parser.parse_args()

print(args.n)

# Creating command line utilities in Python is a straightforward and flexible process thanks to the argparse module. With a few lines of code, 
# you can create powerful and customizable command line tools that can make your development workflow easier and more efficient. Whether you're 
# working on small scripts or large applications, the argparse module is a must-have tool for any Python developer.





















# For creating a Command Line Utility In Python, first import two modules, i.e., argsparse and sys. argsparse helps us to get command-line 
# arguments in our program, and the sys module helps us to import the code we wrote using argparse onto the console. 
# For more details and descriptions about these modules, you can read the python documentation for these modules.

import argparse
import sys


# The argparse module helps us to parse the arguments passed with the  script and process them more conveniently. One of the advantages of using 
# the argparse module is that it makes it easy to write user-friendly command-line interfaces.

# We can use the Python argparse module to create a command-line interface by following these steps:
# Import the Python argparse module
# Create the parser
# Add optional and positional arguments to the parser
# Execute .parse_args()
# When we execute .parse_args(), we will get the Namespace object that contains a simple property for each input argument received from the 
# command line.

# Python provides the sys module that gives us independence from the host machine Operating System and allows us to operate on an underlying 
# interpreter, irrespective of its being a Linux or Windows Platform. With the help of the sys module, we can access system-specific parameters 
# and functions. It provides different functions used to manipulate different parts of the  Python Runtime Environment. To use the sys module, 
# we have to import it so that it brings required sys module dependencies into our scope.

# Code as described/written in the video old one harry



import argparse
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y

    elif args.o == 'mul':
        return args.x * args.y

    elif args.o == 'sub':
        return args.x - args.y

    elif args.o == 'div':
        return args.x / args.y

    else:
        return "Something went wrong"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()   # through argparse , we made a function and add arguments in it through variable 
    
    parser.add_argument('--x', type=float, default=1.0,
                        help="Enter first number. This is a utility for calculation. Please contact harry bhai")

    parser.add_argument('--y', type=float, default=3.0,
                        help="Enter second number. This is a utility for calculation. Please contact harry bhai")

    parser.add_argument('--o', type=str, default="add",
                        help="This is a utility for calculation. Please contact harry bhai for more")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))
