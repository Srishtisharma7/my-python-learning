#1.Write a program to print 1 to 50 using a while loop.
i = 1

while(i<51):
    print(i)
    i +=1 # or i = i + 1


# print "Harry" – 5 times!
i = 0
while (i < 5): 
    print("Harry")
    i = i + 1
#Note: If the condition never become false, the loop keeps getting executed.



#2.list using while

l = [1, "Harry", False, "This", "Rohan", "Shubham", "Shubhi"]
i = 0
#length = 7
while(i<len(l)):     
    print(l[i]) 
    i +=1      
    # i<7 so print  , l(0) = print 1, i++ 
    # similarly ,l(6) = shubham, i++ ,i = 7



    
'''there is no do while loop in python
To create a do while loop in Python, you need to modify the while loop a bit in order to get similar behavior to a do while loop.
The most common technique to emulate a do-while loop in Python is to use an infinite while loop with a break statement wrapped in an 
if statement that checks a given condition and breaks the iteration if that condition becomes true:'''
    
while True:
    number = int(input("Enter a positivenumber: "))
    print (number)
    if not number > 0:
        break

'''This loop uses True as its formal condition. This trick turns the loop into an infinite loop. Before the conditional statement, the loop runs all the required processing and updates the breaking condition. If this condition evaluates to true, 
then the break statement breaks out of the loop, and the program execution continues its normal path.'''   






#3.break and continue
#‘break’ is used to come out of the loop when encountered. It instructs the program to exit the loop now.
for i in range(20):
    if(i == 14):
        break # Exit the loop right now , print till 13 only
    print(i)

#continue’ is used to stop the current iteration of the loop and continue with the next one. 
# It instructs the Program to “skip this iteration” only rest executes.

for i in range(20):
    if(i == 14):
        continue # Skip this iteration , print 12,13,15 skip 14 then 16, 17,....
    print(i)    


#4.pass is a null statement in python. It instructs to “do nothing”.
for i in range(645):
    pass
# without pass, the program will throw an error, if we move to while direct after for written adha adhura 
i = 0
while(i<15):
    print(i)
    i += 1




# while loop with else
i = 0
while i<7:
  print(i)
  i = i + 1
  # if i == 4:
  #   break

else:
  print("Sorry no i")

# if loop gets exhauseted then it prints else statement;
# if it breaks in between , the else statement do not get printed  

