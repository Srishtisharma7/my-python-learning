#Problem 1.Write a python program to display a user entered name followed by Good Afternoon using input () function.

name = input("Enter your name: ")
print(f"Good Afternoon, {name} ") 
#f string mark krke we can add or join two strings, marking f is important otherwise "Good Afternoon, {name} " get printed




# Problem 2. Write a program to fill in a letter template given below with name and date.

letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''

print(letter.replace("<|Name|>", "Srishti").replace("<|Date|", "24 September 2050"))
#chaining of strings ,first replaced name , got a new string then again we replace date from the new stringsrishti