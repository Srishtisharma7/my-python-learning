# 1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

words = {
    "madad": "Help",
    "kursi": "Chair",
    "billi": "Cat"
}
#we take input from user and pass this word variable as a key inside dictionary to get the corresponding value pair
word = input("Enter the word you want meaning of: ")
print(words[word])
#word input should be in the dictionary ,otherwise error 


# 2. Write a program to input eight numbers from the user and display all the unique numbers (once).

s = set()  #typecasting input into int
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  

print(s)
#property of set is to print only unique characters



# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
s = set()
s.add(18)
s.add("18")
print(s)
#output : yes ,{'18', 18}



# 4. What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?  = 2 
print(len(s))
"""
In Python, " comparison operator == checks for equality between two values. When comparing an integer (20) and a floating-point number (20.0), Python evaluates their values and determines if
they are numerically equal. Hence , 20 = 20.0 evaluates to True
and in set they are counted as one so 2 is the length because 1. 20 and 2.string '20'
"""

# 5.What is the type of 's'?  ans  = dictionary
s = {}
print(type(s))



# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

d = {}

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

print(d)
#output :{'meena': 'engish', 'reena': 'hindi', 'srishti': 'german', 'aditya': 'french'}



# 7. If the names of 2 friends are same; what will happen to the program in problem 6?
# The values entered later will be updated as dictionary is mutable 



# 8. If languages of two friends are same; what will happen to the program in problem 6?
# Nothing will happen. The values can be same as in dictionaries keys are the identifiers so they get updated



# 9. Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}
s[4][0] = 9
"""type-error raised"""
# no unhashable type: 'list'[1,2] 
"""sets in Python require all their elements to be immutable and hashable. Lists are mutable and not hashable, so they cannot be added to a set."""
# as list cant be included in set also, if any other particular value we have to change, that also we cant 
# as sets are unindexed we cant access values by their index and update them 