# 1. Write a program to print multiplication table of a given number using for loop.
n = int(input("Enter a number: "))

for i in range(1, 11):  # 1 to 10
    print(f"{n} X {i} = {n * i}")



# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.

l = ["Harry", "Soham", "Sachin", "Rahul"]

for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")
#f-strings (formatted string literals) are a concise and readable way to format strings by embedding expressions directly inside string literals. 


# 3. Attempt problem 1 using while loop.

n = int(input("Enter a number: "))
i = 1
while(i<11):    # 1 to 10
    print(f"{n} X {i} = {n * i}")
    i += 1



# 4. Write a program to find whether a given number is prime or not.
n = int(input("Enter a number: "))
# 1 or n se divide hoke hi if reminder only comes 0 ,its prime 
#otherwise from 2 to n-1 if comes 0 , its not prime
#range (2,n) means from 2 to n-1 only, excluding n

for i in range(2, n):
    if(n%i) == 0:
        print("Number is not prime")
        break       #stop executing the loop , enter else and print the statement
else:
    print("Number is prime")



# 5. Write a program to find the sum of first n natural numbers using while loop.
n = int(input("Enter the number: "))
i = 1   #natural no. start with 1 so from 1 to n
sum = 0
while(i<=n):
    sum += i  # or sum = sum + i 
    i+=1

print(sum)



# 6. Write a program to calculate the factorial of a given number using for loop.
# 5! = 1 X 2 X 3 X 4 X 5

n = int(input("Enter the number: "))
product = 1
for i in range(1, n+1):
    product = product * i

print(f"The factorial of {n} is {product}")   #f string


# 7. Write a program to print the following star pattern.

#       *
#      ***
#     *****    for n = 3


n = int(input("Enter the number: "))
for i in range(1, n+1):      # range includes n also now
    print(" "* (n-i), end="")
    print("*"* (2*i-1), end="")
    print("")

'''or n = 3, (n-i * " ") prints 2 spaces as i= 1 ,so 3-1 = 2, 
then i=2, 3-2 =1 blank spaces, t
hen i=3 so 3-3 = o blank space to print

stars: i=1, 2*1-1 = 1 star
i = 2, 2*2-1 = 3 star
i=3 , 3*3-1 = 5 star

'''
'''end"" does not let another line start after declaring another print statement,we use it to print blank spaces and star in the same line
#one empty print is to switch to next line to continue star pattern printing , didn't use \n  otherwise it will skip one more line 
so empty print moves to next line and prints nothing '''


# 8. Write a program to print the following star pattern:

#      *
#      **
#      *** for n = 3

 
n = int(input("Enter the number: "))
for i in range(1, n+1): 
    print("*"* i, end="")  #no blank space, n(3)lines , print * equal to increasing i
    print("")



# 9. Write a program to print the following star pattern.

#        ***
#        * *          for n = 3, try for n = 7
#        ***

n = int(input("Enter the number: "))
for i in range(1, n+1): 
    if(i==1 or i==n):
        print("*"* n, end="")  # start and end line me n stars print , rest;
    else:
        print("*", end="")                  # print * , end"" to not move to next line
        print(" "* (n-2), end="")           # print blank (n-2) as two spaces are for star printed start me or end me
        print("*", end="")                  # print *, end  and print empty , switch to next line and continye to next loop iteration
    print("")                               # for new line



# 10. Write a program to print multiplication table of n using for loops in reversed order.
n = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{n} X {11 -i} = {n*(11-i)}")
'''reverse means start from 10 so, range me we include 11 to include 10 tk, 
here also 11-i when i = 1 gives 10 to start with and it gets multiplied with n also to get a table 2'''