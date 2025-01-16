from module import callfunction
callfunction()

# output when importing callfunction :

# The module has been successfully imported!
# module                   [is the name of file from where it is run] as it is imported, otherwise __name__ is set main
# This is a message from callfunction()


'''__name__special variable in Python, which helps determine whether the code is being executed directly or imported as a module.
When a Python file is executed directly, the value of __name__ is set to "__main__".

 If the Python file is imported as a module into another script, the value of __name__ is set to the module's name (e.g., the name of the file without the .py extension).

The output will not include the print("We are directly running this code") and myFunc() call. Instead, it will only show the output of the imported file if there are any top-level statements in the module. 
The __name__ in this case will be "module" (the name of the module, without the .py extension), so it would print "module" instead of "__main__".'''







a = 89    # global variable

def fun(): 
    # global a  (globalize a value to 3 from 89)
    a = 3    # local variable
    print(a)

fun()
print(a)

x = 10  # global variable

'''example 2'''

def my_function():
  global x
  x = 5  # this will change the value of the global variable x
  y = 5  # local variable


my_function()
print(x)  # prints 5
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function







'''Enumerate'''

l = [3, 513, 53, 535]

# index = 0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index += 1

# This can be simplified using enumerate function
# enumerate() takes an iterable (like a list) and returns an iterator that produces pairs of index and the corresponding item.
# In the for loop, enumerate(l) provides a tuple (index, item) on each iteration.
# index will hold the current index (position in the list) and item will hold the value at that position
for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")

# it eliminates the potential for mistakes, such as forgetting to increment the index or having to manage an external counter.

# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)
# 0 apple
# 1 banana
# 2 mango


'''By default, the enumerate function starts the index at 0, but you can specify a different starting index by passing it as an argument to the enumerate function:'''

# Loop over a list and print the index (starting at 1) and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# This will output:

# 1 apple
# 2 banana
# 3 mango


