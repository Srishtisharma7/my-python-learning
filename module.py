def myFunc():
    print("Hello world!")

if __name__ == "__main__":                  # only then print
    # If this code is directly executed by running the file its present in
    print("We are directly running this code")  # this prints only when directly run this file
    myFunc()
    print(__name__)


# The if __name__ == "__main__": block will only execute if the file is being run directly (not imported as a module)
# When a Python file is executed directly, the value of __name__ is set to "__main__".
# If the Python file is imported as a module into another script, the value of __name__ is set to the module's name (e.g., the name of the file without the .py extension).    

# The if __name__ == "__main__": construct allows you to write code that can be used both as a standalone script and as a reusable module in other programs.
# This way, functions and classes defined in the script can be imported into other scripts without running the code under the if __name__ == "__main__": block.


# Message to be printed when the module is imported
print("The module has been successfully imported!") # print while importing as well

def callfunction():    # prints this function also while importing since it has no condition
    print(__name__)    # prints module but not here, in the directory where it is imported
    print("This is a message from callfunction()")


# output: 
# We are directly running this code
# Hello world!
# __main__ (name of file as directly running here)
# The module has been successfully imported