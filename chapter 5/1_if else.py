a = int(input("Enter your age: "))

# If elif else ladder
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid negative age")

elif(a==0):
    print("You are entering 0 which is not a valid age")    

else:
    print("You are below the age of consent")


print("End of Program")


applePrice = 10
budget = 200
if (budget - applePrice > 50):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")



num = int(input("Enter the value of num: "))
if (num < 0):
  print("Number is negative.")
elif (num == 0):
  print("Number is Zero.")
elif (num == 999):
  print("Number is Special.")
else:
  print("Number is positive.")

print("I am happy now")



# short hand if -else can be used when the condition being tested is simple and the code blocks to be executed are short. 

a = 330000
b = 3303
print("A") if a > b else print("=") if a == b else print("B")

c = 9 if a>b else 0
print(c)