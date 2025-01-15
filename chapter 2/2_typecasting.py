#type and typecasting

a = 31
type(a) # class ‹int›
b = "31.2"
type (b) # class ‹str› as double quotes


# Implicit TypeCasting
c = 1.9
d = 8

print(c + d)

"""A number can be converted into a string and vice versa (if possible)
There are many functions to convert one data type into another."""

# str (31)=>"31"              # integer to string conversion (string always in double quote)
# int ("32") => 32            # string to integer conversion
# float（32） = 32.0          # integer to float conversion (int,str,and float are all functions for typecasting)

a = input("Enter number 1: ")
b = input("Enter number 2: ")      #takes input from user

print("Number a is: ", a)         #5 or srishti
print ("Number b is: ", b)        #7 or sharma
print("Sum is ", a + b)         #shows sum 57 instead of 12  and 'srishtisharma'as it consider the values as strings 


#for this we typecast the values of input into into
a = int(input ("Enter number 1: "))
b = int(input("Enter number 2: "))
print( "Number a is: ", a)
print ("Number b is: ", b)
print("Sum is ", a + b)     #now 5+7 = 12 as inputs are typecasted into int


#problem
""" Check the type of variable assigned using input () function."""

a =input("Enter the value of a")
print(type(a))
#every input value through keyboard is string only 32 or aditya or 32.4