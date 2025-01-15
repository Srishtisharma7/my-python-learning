# Importing in Python is the process of loading code from a Python module into the current script. 
# This allows you to use the functions and variables defined in the module in your current script, as well as any additional modules that the imported module may depend on.

# to import the math module, which contains a variety of mathematical functions, you would use the following statement:
import math


#to import only the sqrt function from the math module
result = math.sqrt(9)
print(result)  # Output: 3.0




# to import only the sqrt function from the math module, you would write:

from math import sqrt

result = sqrt(9)
print(result)  # Output: 3.0




# You can also import multiple functions or variables at once by separating them with a comma:
from math import sqrt, pi
result = sqrt(9)
print(result)  # Output: 3.0

print(pi)  # Output: 3.141592653589793




# importing everything
# It's also possible to import all functions and variables from a module using the * wildcard. However, this is generally not recommended as it can 
# lead to confusion and make it harder to understand where specific functions and variables are coming from.

from math import *
result = sqrt(9)
print(result)  # Output: 3.0
print(pi)  # Output: 3.141592653589793




# Python also allows you to rename imported modules using the as keyword. This can be useful if you want to 
# use a shorter or more descriptive name for a module, or if you want to avoid naming conflicts with other modules or variables in your code.

import math as m

result = m.sqrt(9)        # accessing functions using as keyword
print(result)  # Output: 3.0  
print(m.pi)  # Output: 3.141592653589793




# The dir function
# Finally, Python has a built-in function called dir that you can use to view the names of all the functions and variables defined in a module. 
# This can be helpful for exploring and understanding the contents of a new module.

import math
print(dir(math))


# This will output a list of all the names defined in the math module, including functions like sqrt and pi, as well as other variables and constants.