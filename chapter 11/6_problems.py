# 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present,
# a message without exiting the program must be printed prompting the same.

try:
    with open("1.txt", "r") as f:
        print(f.read())
except Exception as e: 
    print(e)                      # e is the variable that holds the exception object when an error occurs within the try block.
                                  # It contains information about the type of error and an error message describing what went wrong.

try:
    with open("2.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("3.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)


print("Thank You!")

# or

'''file_names = ["1.txt", "2.txt", "3.txt"]

for file_name in file_names:
    try:
        with open(file_name, "r") as f:
            print(f"{file_name} content:")
            print(f.read())
    except Exception as e:
        print(f"Error reading {file_name}: {e}")

print("Thank You!")'''

# [Errno 2] No such file or directory: '1.txt'
# [Errno 2] No such file or directory: '2.txt'
# [Errno 2] No such file or directory: '3.txt'                      <- output
# Thank You!







# 2. Write a program to print third, fifth and seventh element from a list using enumerate function.

l = [1, 2, 3, 4, 5, 6 ,7 , 8]

for i, item in enumerate(l):
    if i == 2 or i == 4 or i == 6:
        print(item)

# the enumerate() function provides both the index (i) and the value (item) of each element in the list as you iterate through it.
# 3 5 7




# 3. Write a list comprehension to print a list which contains the multiplication table of a user entered number.

n = int(input("Enter a number: "))

table = [n*i for i in range(1, 11)]
print(table)

# Stores each result in a list, generating the multiplication table for n.
# using for loop :

n = int(input("Enter a number: "))

table = []
for i in range(1, 11):
    table.append(n * i)

print(table)
# output : [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]




# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a/b)
except ZeroDivisionError as v:
    print("Infinite")




# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.

n = int(input("Enter a number: "))

table = [n*i for i in range(1, 11)]
with open("/Users/srishtisharma/python/code harry/chapter 11/tables.txt", "a") as f:                 # opening the file in append mode
    f.write(f"Table of {n}: {str(table)} \n")

# uses list comprehension to create table in a list
# the with statement ensures the file is properly closed after the operation, even if an error occur