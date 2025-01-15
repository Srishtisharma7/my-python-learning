"""Problem 3. Write a program to detect double space in a string."""

name = "Harry is a good  boy and  "

print(name.find("  "))
#return -1 if no double space found ,
# otherwise return the index value of substring we are finding in its parent string

"""Problem 4. Replace the double space from problem 3 with single spaces."""

name = "Harry is a good  boy and  "

print(name.replace("  ", " "))  
print(name) #returns original string

# Strings are immutable which means that you cannot change them by running functions on them
#name string remains same , everytime new string is run and executed


"""Problem 5. Write a program to format the following letter using escape sequence characters."""
# letter = "Dear Harry, this python course is nice. Thanks!"


letter = "Dear Harry,\n\tThis python course is nice.\nThanks!"
print(letter)