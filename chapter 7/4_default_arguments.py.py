# Default arguments

'''We can have a value as default as default argument in a function.
If we specify name = “stranger” in the line containing def, this value is used when no
argument is passed.'''
# Example:

def greet(name = "stranger"):
 print("Welcome " + name)

greet("srishti")     #function call 0 identation
greet()              #now deafault stranger value is passed
                 

#Example 2:

def goodDay(name, ending="Thank you"):
    print(f"Good Day, {name}")
    print(ending)

goodDay("Harry", "Thanks")
goodDay("Rohan")    
#no ending argument passed,so it accepted default value 'thank you'




def name(fname, mname = "Jhon", lname = "Whatson" ):
   print("Hello,", fname, mname, lname)
name ("Amy")





'''Keyword arguments:'''
# We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name.
# Hence, the the order in which the arguments are passed does not matter.
# Example:

def name(fname, mname, Iname):
   print("Hello,", fname, mname, Iname)
name(mname = "Peter", Iname = "Wesker", fname ="Jade")




'''Required arguments'''
# In case we don't pass the arguments with a key = value syntax,
# then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.
# Example 1: when number of arguments passed does not match to the actual function definition.
def name(fname, mname,lname):
   print( "Hello,",fname, mname,lname)

name ("Peter", "Quill" , "davidson")


# Example 3:

def average(a, b, c=1): #c default , a nd b required
    print("The average is ", (a + b + c) / 2)
average (5, 6)





'''variable length arguments'''
# Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.
# There are two ways to achieve this:
# Arbitrary Arguments:
# While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.
# Example:

def average(*numbers):
  # print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  print("Average is: ", sum / len(numbers))
  # return 7
  return sum / len(numbers)     # apart from printing it stores also for future use

average (5, 6, 7, 1)  # n arguments passed


# example 2:
def name(*name):
   print(type(name))  # return as tuple
   print( "Hello,", name[0], name[1], name[2])
name ("James","Buchanan", "Barnes")


def name(**name):
  print(type(name))  # dictionary
  print("Hello,", name["fname"], name["mname"], name["lname"])


name(mname="Buchanan", lname="Barnes", fname="James")