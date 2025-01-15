# Function with no return value

def goodDay (name, ending):
    print ("Good Day," + name ) 
    print (ending)
a = goodDay ("Harry", "Thank you")
print(a)

# a variable none, if we want to assign a value to the variable when function is called , we return something in the function definition

def goodDay (name, ending):
    print ("Good Day," + name)
    print (ending)
    return "ok"
a = goodDay ("Harry", "Thank you")
print(a)

# return ok to a variable