# A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of 
# the original function. The new function is often referred to as a "decorated" function. 

#One common use of decorators is to add logging to a function. For example, you could use a decorator to log the arguments and return value of a function each time it is called:

import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b

# In this example, the log_function_call decorator takes a function as an argument and returns a new function that logs the function 
# call before and after the original function is called.

#example 2


def greet(fx):    # its a decorator function we made , nested functions insides
  def mfx():
    print("Good Morning")
    fx()
    print("Thanks for using this function")
  return mfx      # returning a function to the decorator function only

@greet
def hello():
  print("Hello world")
hello()

# greet(hello)() similar to above thing






def greet(fx):
  def mfx(*args, **kwargs):   # decorator function with args and kwargs which take arguments in tuple and dictionary ** key :value formats
    print("Good Morning")
    fx(*args, **kwargs)
    print("Thanks for using this function")
  return mfx


@greet # set decorator (either do this)
def add(a, b):
  print(a+b)
add(1, 2)  
# same as
# greet(add)(1, 2)  (or this as here also add passed to greet funvtion so both gonna process)
# # yha arguments dene ka no fayda if decorator me args or kwargs nhi lgaya






'''Args and kwargs'''

# def function_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)                      if we have to print more names , we have to make multiple changes in the print section as well as arguments section
# so instead we pass all the items through a list [] or a tuple () through *args and key value dictionary pairs through **kwargs 


# function definition with types of arguments defined

def funargs(normal, *argsrohan, **kwargsbala):   # args , argsno , argsrohan , kwargs , kwargsbala any convention is good but make sure to use that everywhere in the code
    print(normal)
    # a normal argument is always written first , followed by args and kwargs

    for item in argsrohan:
        print(item)
    print("\nNow I would Like to introduce some of our heroes")
    for key, value in kwargsbala.items():
        print(f"{key} is a {value}")


# function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam")

har = ["Harry", "Rohan", "Skillf", "Hammad",
       "Shivam", "The programmer"]
normal = "I am a normal Argument and the students are:"
kw = {"Rohan":"Monitor", "Harry":"Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam":"Cook"}
funargs(normal, *har, **kw)    # calling function , passing actual arguments
  

'''args is a short form used for arguments. It is used to unpack an argument. In the case of *args, the argument could be a list or tuple. Suppose that we have to enter the name of 
students who attended a particular lecture. Each day the number of students is different, so positional arguments would not be helpful because we can not leave an argument empty in 
that case. So the best way to deal with such programs is to define the function using the class name as formal positional argument and student names with parameter *args. In this way, 
we can pass student's names using a tuple.
Note that the name args does not make any difference, we can use any other name, such as *myargs. The only thing that makes a difference is the Asterisk(*).


**kwargs:

The full form of **kwargs is keyword arguments. It passes the data to the argument in the form of a dictionary. Let's take the same example we used in the case of *args. The only difference 
now is that the student's registration, along with the student's name, has to be entered. So what **kwargs does is, it sends argument in the form of key and value pair. So the student's name 
and their registration both can be sent as a parameter using a single ** kwargs statement.
Same as we discussed for args*, the name kwargs does not matter. We can write any other name in its place, such as **attendance. The only mandatory thing is the double asterisks we placed before the name.   
One of the instances where there will be a need for these keyword arguments will be when we are modifying our code, and we have to make a change in the number of parameters or a specific function.'''











'''Static methods'''

# Example : 

class Math:
  def __init__(self, num):
    self.num = num

  def addtonum(self, n):
    self.num = self.num +n          # self agar removed, it wud show error
    
  @staticmethod
  def add(a, b):             # it is used in the class in order to ship it as it is to other programs and also to let it stay associated with the class,that is why we add static method to the function and define it in a class
      return a + b                # no need of self here ,it is used when no need for class instance 

# result = Math.add(1, 2)     we can define add function normally as well, but then it wont get passed wrt to class math defined
# print(result) # Output: 3
a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)

print(Math.add(7, 2)) 