'''match case ; similar to switch case in other programming languages'''

def http_status(status):     # The function http_status takes one argument, status.
    match status:            # The match statement evaluates the value of status and attempts to match it against the patterns defined in the case blocks.
        case 200: 
            return "OK" 
        case 404: 
            return "Not Found" 
        case 500: 
            return "Internal Server Error" 
        case _: 
            return "Unknown status"   # The _ is a wildcard that matches anything not explicitly handled in the previous cases.
# If status does not match 200, 404, or 500, it falls back to this case, and the function returns "Unknown status".


print(http_status(5007))    # function called
# 5007 is wildcard case, it will return 'unknown status'

'''Example 2'''

def check_input(data):
    match data:
        case int() if data > 0:
            return "Positive integer"
        case int() if data < 0:
            return "Negative integer"
        case str():
            return "String"
        case list():
            return "List"
        case _:
            return "Unknown type"

print(check_input(42))      # Output: Positive integer
print(check_input(-10))     # Output: Negative integer
print(check_input("hello")) # Output: String
print(check_input([1, 2]))  # Output: List










'''DICTIONARY MERGE & UPDATE OPERATORS'''
# New operators and  allow for merging and updating dictionaries.


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 , dict2
print(merged) # Output: {'a': 1, 'b': 3, 'c': 4}

# If there are duplicate keys (like 'b' in this example), the value from the second dictionary (dict2) takes precedence.





'''You can now use multiple context managers in a single with statement more cleanly
using the parenthesised context manager'''

with(
    open('/Users/srishtisharma/python/code harry/chapter 8/1_file.py') as f1,
    open('/Users/srishtisharma/python/code harry/chapter 8/2_file_write.py') as f2
):            # with (with) staement we need to write a code below it as well telling what to do after this is executee 
    data = f1.read()
    print(data)
# Process files

# Two files (file1.txt and file2.txt) are opened within a single with statement.
# The parentheses let you clearly group multiple context managers in a readable way.
# Both f1 and f2 are closed automatically when the with block ends.    



'''helper functions'''

#The dir() method

'''dir(): The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. 
It is a useful tool for discovering what you can do with an object. Example:'''

x = [1, 2, 3]
print(dir(x))

#['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
#  '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', 
# '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 
# 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

#The __dict__ attribute

'''__dict__: The __dict__ attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection. Example:'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("John", 30)
p.__dict__

#Output : {'name': 'John', 'age': 30}


#The help() mehthod

'''help(): The help() function is used to get help documentation for an object, including a description of its attributes and methods. Example:'''
# gives whole documentation

help(str)
# Help on class str in module builtins:

# class str(object)
#  |  str(object='') -> str
#  |  str(bytes_or_buffer[, encoding[, errors]]) -> str
#  |
#  |  Create a new string object from the given object. If encoding or
#  |  errors is specified, then the object must expose a data buffer
#  |  that will be decoded using the given encoding and error handler.
#  |  Otherwise, returns the result of object.__str__() (if defined)
#  |  or repr(object).
#  |  encoding defaults to sys.getdefaultencoding().
#  |  errors defaults to 'strict'.