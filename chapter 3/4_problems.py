# 1. Write a program to store seven fruits in a list entered by the user.
fruits = []

f1 = input("Enter Fruit name: ")
fruits.append(f1)
f2 = input("Enter Fruit name: ")
fruits.append(f2)
f3 = input("Enter Fruit name: ")
fruits.append(f3)
f4 = input("Enter Fruit name: ")
fruits.append(f4)
f7 = input("Enter Fruit name: ")
fruits.append(f7)
f5 = input("Enter Fruit name: ")
fruits.append(f5)
f6 = input("Enter Fruit name: ")
fruits.append(f6)

print(fruits)
#output:['Apple', 'Banana', 'Mango', 'Grapes', 'Orange', 'Litchi', 'Guava']



# 2. Write a program to accept marks of 6 students and display them in a sorted manner.
marks = []
#typecasting input string into int , otherwise alphabetically sort happens
f1 = int(input("Enter Marks here: "))
marks.append(f1)
f2 = int(input("Enter Marks here: "))
marks.append(f2)
f3 = int(input("Enter Marks here: "))
marks.append(f3)
f4 = int(input("Enter Marks here: "))
marks.append(f4)
f5 = int(input("Enter Marks here: "))
marks.append(f5)
f6 = int(input("Enter Marks here: "))
marks.append(f6)

marks.sort()

print(marks)



# 3. Check that a tuple type cannot be changed in python.
#a = (34, 234, "Harry")
#a[2] = "Larry"
#will show error tuple object does not support assignment

# 4. Write a program to sum a list with 4 numbers.
l = [3, 3, 5, 1]
print(sum(l))


# 5. Write a program to count the number of zeros in the following tuple:
a = (7, 0, 8, 0, 0, 9)
n = a.count(0)
print(n)
