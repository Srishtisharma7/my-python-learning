# 1. Write a program using functions to find greatest of three numbers.

def greatest(a, b, c):
    if(a>b and a>c):
        return a         # return a to function or variable
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c

a = 1
b = 23
c = 3

print(greatest(a, b, c))        # function k andr pura logic likh ke , just call it



# 2. Write a python program using function to convert Celsius to Fahrenheit.
#Simple code:

def f_to_c(f):
    return 5*(f-32)/9
f = int(input("Enter temperature in F: "))
print(f_to_c(f))
#or also use f string
print(f"{f_to_c(f)} Degree C")
#we can round the output value as well, so we can write 
print(f"' {round(f_to_c(f), 2)} °")

#notice the differnec in 3 print statements:
# 1.37.77777777777778
# 2.37.77777777777778 Degree C
# 3.' 37.78 °

#Fancy code:

def f_to_c(f):
    return 5*(f-32)/9    # return to celcius

f = int(input("Enter temperature in F: "))
c = f_to_c(f)          # to enhance readability funcn passed to vaiable c
print(f"{round(c, 2)}°C") 

# output: ' 37.78 °

# 3. How do you prevent a python print() function to print a new line at the end.

print("a")
print("b")
print("c", end="")
print("d", end=""), 



# 4. Write a recursive function to calculate the sum of first n natural numbers.
'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5

sum(n) = 1 + 2 + 3 + 4.... n -1 + n
sum(n) = sum(n-1) + n
'''

def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n
print(sum(4))

'''a base condition to return is given so that n-1 krte krte 2-1 ,1-1 ,0-1 tak negative me bhi loop ka sum na jaye, so to stop the function'''


# 5. Write a python function to print first n lines of the following pattern:
# ***
# **          - for n = 3
# *

def pattern(n):
    if(n==0):
        return         #n=0 , return means execution stop,otherwise print n times star, 3 to 3 star, then decrease by 1 , n=2 to 2 star
    print("*" * n)
    pattern(n-1)
pattern(3)



# 6. Write a python function which converts inches to cms.

def inch_to_cms(inch):                  #function defined, inch as argument
    return inch * 2.54                   # return value to function

n = int(input("Enter value in inches: "))

print(f"The corresponding value in cms is {inch_to_cms(n)}")               # returned value inch(n)* 2.54



# 7. Write a python function to remove a given word from a list and strip it at the same time.

def rem(l, word):      # list and word to remove passed as argument
    for item in l:     #loop to iterate over each item in list
        l.remove(word)           
        return l              # after removal , returned to l list updated
    
l = ["Harry", "Rohan", "Shubham","an"]
print(rem(l, "an"))            # funcn call , an and list passed as argument and output gives updated list     

# removes 'an' from the list , but to further strip

def rem(l, word):
    n = []                         # new list made
    for item in l:
        if not(item == word):           # instead of removing the word , we strip it , if it matches with the list items
            n.append(item.strip(word))  # or if not matches , append it to the new list [n] and return it
            #this ensures we skip adding the word itself to the resulting list.
    return n

l = ["Harry", "Rohan", "Shubham", "an"] 
print(rem(l, "an"))           # funcn call , an and list passed as argument and output gives updated list     

# ['Harry', 'Rohan', 'Shubham']: output 1
# ['Harry', 'Roh', 'Shubham'] : output 2



# 8. Write a python function to print multiplication table of a given number.

def multiply(n):                       #function defined with proper logic inside
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")     #string catenation as print like 5 x 1 = 5 or (n*i)

multiply(5)                            #function called