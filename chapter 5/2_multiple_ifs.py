a = int(input("Enter your age: "))

# If statement no: 1
if(a%2 == 0):
    print("a is even")
# End of If statement no: 1 executes independently, 
#else and elif statements cant be executed independtly , they are always connected to if statemnet

# If statement no: 2
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid negative age")  

else:
    print("You are below the age of consent")
# End of If statement no: 2 executes with elif and else statements

print("End of Program")

# 1. There can be any number of elif statements.
# 2. Last else is executed only if all the conditions inside elifs fail.

'''nested ifs'''

num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")