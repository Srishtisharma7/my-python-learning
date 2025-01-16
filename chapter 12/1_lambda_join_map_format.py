'''Lambda function'''

# def square(n):
# return n*n , instead

square = lambda x: x*x   # [input parameters : return result after evaluation]

print(square(5))
# returns 25

sum = lambda a,b,c: a+b+c
sum (1,2,3) # returns 6

# Lambda function to calculate the product of two numbers,
# with additional print statement
lambda x, y: print(f'{x} * {y} = {x * y}')

def appl(fx, value):
  return 6 + fx(value)

print(appl(lambda x: x * x , 2))
# can be passed into a function as well

#Lambda functions are anonymous, meaning they don’t have a name unless you assign them to a variable (like square or sum in your example).
# A lambda function can only contain a single expression, which is returned automatically.




'''Join function
requires that all elements in the iterable are strings. If not, you'll get a TypeError.'''
# f your list contains non-string items, convert them first:
# concatenate the elements of an iterable (like a list) into a single string, with a specified separator.

a = ["Harry", "Rohan", "Shubham"]

final = "::".join(a)   # The join() method combines all elements of the list a into a single string.
print(final)                      # The separator (::) is placed between each element


l = ["apple", "mango", "banana"]
result = ", and, ".join(l)
print(result)

# Here, the string ", and, " is used as the separator.
# The result is a concatenated string where , and, appears between each fruit name.
# The above line will return “apple,and,mango,and,banana”.

# If you don’t want any separator, use an empty string as the separator:
chars = ["H", "e", "l", "l", "o"]
word = "".join(chars)
print(word)  # Output: "Hello"




'''Format function'''

a = "{1} is a good {0}".format("harry", "boy")      # The format() method replaces these placeholders with the arguments provided
a = "{0} is a good {1}".format("harry", "boy")

print(a)

# You can also use named placeholders with keyword arguments:

msg = "{name} is a {adjective}".format(name="Alice", adjective="genius")
print(msg)  # Output: "Alice is a genius"

letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Harry"

print(letter.format(country, name))
print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")   # use double brackets to show in code
price = 49.09999
txt = f"For only {price:.2f} dollars!"           # 2 float only value
print(txt)
# print(txt.format())
print(type(f"{2 * 30}"))      # f string allow us to compute expression in the string as well




'''Map, filter ,reduce'''

from functools import reduce
# Map Example 
l = [1, 2, 3, 4, 5]     # Apply a function (square) to each element in the list l.

# newl = []
# for item in l:
# newl.append(square(item))        instead of this , we can map function to all

square = lambda x: x*x

sqList = map(square, l)     # map returns a map object, which is converted to a list using list().
print(list(sqList))         # The result is the list of squares of numbers in l.




# Filter Example
# Filter elements in the list l based on the condition in the even function.

def even(n):               # The even function checks if a number is divisible by 2.
    if (n%2 == 0):
        return True 
    return False

onlyEven= filter(even, l)       # filter(even, l) returns only the elements of l for which even(n) is True.
print(list(onlyEven))




# Reduce Example
# Aggregate the list l into a single value using the reduce function.
# reduce takes a function and a sequence and applies the function cumulatively to the elements of the sequence.

def sum(a, b):
    return a + b     # reduce(sum, l) computes 1 + 2 + 3 + 4 + 5 = 15.

mul = lambda x,y:x*y     # reduce(mul, l) computes 1 * 2 * 3 * 4 * 5 = 120.

print(reduce(sum, l))
print(reduce(mul, l))

'''
map: Transforms elements in a sequence using a function.
Example: Applying a transformation like squaring.

filter: Selects elements from a sequence that satisfy a condition.
Example: Keeping only even numbers.

reduce: Combines elements of a sequence into a single result by applying a function repeatedly.
Example: Calculating a sum or product.
'''


# is vs ==
# both comparison operators

a = None
b = None

print(a is b) # exact location of object in memory
print(a is None) # exact location of object in memory as compiler do not waste memory for constants as they'll not change
print(a == b) # checks for value

# strings and integers are immutable, which means that once they are created, their value cannot be changed. 
# This means that, for strings and integers, is and == will always return the same result:
a = "hello"
b = "hello"

print(a == b)  # True
print(a is b)  # True

a = 5
b = 5

print(a == b)  # True
print(a is b)  # True
#mutable objects such as lists and dictionaries, is and == can behave differently.


a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False
# a and b are two separate lists that have the same values, so == returns True. However, a and b are not the same object in memory, so is returns False.