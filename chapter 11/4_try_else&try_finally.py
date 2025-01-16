'''Raising exceptions : how to handle division by zero in Python by using the raise statement to manually trigger a ZeroDivisionError'''

a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if(b == 0):
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")       # a custom message is printed
else:
    print(f"The division a/b is {a/b}")

    

a = int(input("Enter any value between 5 and 9"))

if(a<5  or a>9):
  raise  ValueError("Value should be between 5 and 9")
     

# perform division if valid int input of a and b
# in the if condition , f the second number (b) is zero, the program raises a ZeroDivisionError.
# The raise statement manually triggers an exception when division by zero is attempted.
# necessary as it enhances the clarity of the error, helping users understand why the operation isn't allowed.

'''Python already has a built-in ZeroDivisionError, which is raised when division by zero happens.
However, by using raise, you're customizing how the error is raised and providing a more specific message.'''
# its exception handling
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter second number: "))
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    print(f"The division a/b is {a/b}")
except ZeroDivisionError as e:
    print(f"Error: {e}")






'''Try-else''' # works when try is executed correctly, it goes in else  
# else block, which is executed only if no exceptions are raised inside the try block.

try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except Exception as e:
    print(e)   # exception message


else:
    print("I am inside else")



'''Try-finally'''

def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return
    
# The function returns after printing the value, but before exiting, the finally block will be executed.
     
    except Exception as e:
        print(e) 
        return
# Even if a return statement is used in the except block, the finally block will still execute before the function exits.

    finally:
        print("Hey I am inside of finally") # if no function defined, it is always executed, like a normal print statement outside try and except block
# but finally it even executes after functions retruns a  value ,generally below code of function wriiten after return like normal print statement ,
# doesnt work but finlly statement overrides it and in adverse situations also it runs;

main()  

# The finally block always runs, no matter what. This makes it ideal for clean-up tasks like closing files, releasing resources, or printing certain messages (like the one in the example).
# The finally block is typically used for clean-up actions such as closing files, releasing network connections, or printing logs.

# example 2:

def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")
  # print("I am always executed")


x = func1()
print(x)