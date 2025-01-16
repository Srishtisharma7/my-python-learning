'''Using walrus operator(:=) '''

# Also called the assignment expression

# It allows you to assign a value to a variable as part of an expression, making the code more concise and readable.

if (n := len([1, 2, 3, 4, 5])) > 3: 
    print(f"List is too long ({n} elements, expected <= 3)") # Output: List is too long (5 elements, expected <= 3)

'''
len([1, 2, 3, 4, 5]) calculates the length of the list, which is 5.
The result (5) is assigned to the variable n using the walrus operator (:=).
Since 5 > 3, the condition evaluates to True, and the block inside the if statement is executed.
'''
# With the walrus operator, the assignment (n = len(...)) and the condition (n > 3) are combined into a single line,
#  making the code cleaner and more compact.

# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# print(happy := True)

# foods = list()
# while True:
#   food = input("What food do you like?: ")
#   if food == "quit":
#       break
#   foods.append(food)       instead

foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)








'''Type definitions'''

# allow you to indicate the types of variables, function arguments, and return values. 
# Type hints are added using the colon (:) syntax for variables and the -> syntax for function return types.

# Variable type hint [age is a variable, and the type hint : int specifies that it is expected to hold an integer value.
# 25 is assigned to age, so the type matches the hint.]

age: int = 5

# Function type hints

'''name: str: Indicates that the function argument name should be a string.
-> str: Specifies that the function returns a string.'''

def greeting(name: str) -> str:
    return f"Hello, {name}!"
# Usage
print(greeting("Alice")) 
# f you call greeting("Alice"), "Alice" is passed to name, 
# and the function returns the string "Hello, Alice!".


'''Example 2'''

def add_numbers(a: int, b: int) -> int: # function should take int values and return int too
    return a + b

result: int = add_numbers(5, 3)   #result should be int
print(result)  # Output: 8



'''Example 3'''

from typing import List, Tuple, Dict, Union
# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]         # Helps ensure that only integers are stored in the numbers list.
# If you try to add a string (numbers.append("text")), a linter will raise a warning.


# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)      # Useful for representing fixed-size collections where the types of elements are known and fixed.
# If you try to add or remove elements or use the wrong types, a linter will warn you.

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}  # Helps clarify the structure of dictionaries, ensuring keys and values are of the correct types.
# Prevents assigning keys or values of unsupported types.

# Union type for variables that can hold multiple types
identifier: Union[int, str] = "ID123"            # Useful for variables that can take on multiple types, e.g., IDs that may be numeric or alphanumeric.
# Ensures only the specified types (int or str) are used.


'''Benefits of Type Hints:
Clarity:
Type hints make the expected types of variables, function arguments, and return values explicit.

Tool Support:
IDEs and linters can provide better autocompletion, error checking, and warnings.

Documentation:
Type hints act as a form of self-documentation, making the code easier to understand.

Error Detection:
Tools like mypy can analyze code and detect type mismatches at development time, reducing runtime errors.'''



'''python comprehensions'''

# ls = []
# for i in range(100):
#     if i%3==0:
#         ls.append(i)

# ls = [i for i in range(100) if i%3==0]
#
# print(ls)


# dict1 = {i:f"item {i}" for i in range(1, 10001) if i%100==0}
# dict1 = {i:f"Item {i}" for i in range(5)}
#
# dict2 = {value:key for key,value in dict1.items()}
# print(dict1,"\n", dict2)

# dresses = [dress for dress in ["dress1", "dress2","dress1",
#                                "dress2","dress1", "dress2"]]
# print(type(dresses))

evens = (i for i in range(100) if i%2==0)
# print(evens.__next__())

# for item in evens:
#     print(item)







