#try block is where you place statements that might raise an exception.
# if the input is not a valid integer, it will raise a ValueError.

try:
    a = int (input ("Hey, Enter a number: "))
    print(a)      # if i enter int value only try block gets executed and no control to the except block

# if i enter a string here instead of int
# If an exception occurs in the try block, the control is passed to the except block.
# The except Exception as e: part catches the exception and assigns it to the variable e.
# print(e) will display the error message generated by the exception.

# If the user enters "abc" instead of a number, the error message invalid literal for int() with base 10: 'abc' will be displayed.

except Exception as e:
    print (e)   # it wud print the exception

print ("Thank You")      # thank you will also be printed

#without exception, code will fail and just show unknown error to the user

''' Using try-except Prevents the program from crashing due to invalid input or runtime errors.
Provides a way to gracefully handle errors and inform the user about what went wrong.'''

# example :

a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")
try:
  for i in range(1, 11):
    print(f"{int(a)} X {i} = {int(a)*i}")         # give input srishti
except:
  print("Invalid  Input!")

print("Some imp lines of code")
print("End of program")          #without except code do not run forward lines like here ,so exception use comes handy



try:
    num = int(input("Enter an integer: "))
    b = [6, 3]
    print(b[num])
except ValueError:
    print("Number entered is not an integer.")
    
except IndexError:      
  print("Index Error")










# Example 2: How to handle errors nd exceptions

try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except ValueError as v:    # This block will catch a ValueError, which occurs if the user inputs a value that cannot be converted to an integer (e.g., "abc").
    print("Heyyyy")
    print(v)

# and then The exception object (v) is printed, which will contain details about the error (such as "invalid literal for int()").
# The message "Heyyyy" will also be printed to indicate that an error has occurred
    
except Exception as e:
    print(e)
# This block is a "catch-all" that will handle any other exception not previously caught by the specific except block (like ValueError).
# If any unexpected error occurs, it will print the exception message (e).

print("Thank You")
#Regardless of whether an exception occurred or not, the program will print "Thank You" after the try-except block.









