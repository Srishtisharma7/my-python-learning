print(1)
print(2)
print(3)
print(4)
print(5)

# The same task can be done like this:
for i in range(1, 6):   #just like indexes 1 to 6 will print 1 to 5 excluding 6
    print(i)


#2.The range() function in python is used to generate a sequence of number.
# We can also specify the start, stop and step-size as follows:
# range(start, stop, step_size)
# step_size is usually not used with range() 
'''similar to string slicing like range(0,100,4) wud mean 0 to 100 all numbers with 4 step in between like 0,4,8,12,16...'''

for i in range(4):        #(4) means (0:4) , prints 0 to (n-1)3 excluding 4
    print(i)



##A for loop is used to iterate through a sequence like list, tuple, or string [iterables]
# 3. For Loop with Lists
l = [1, 4, 6, 234, 6, 764]
for i in l:
    print(i)

## For Loop with Tuples
t = (6, 231, 75, 122)
for i in t:
    print(i)

## For Loop with Strings
s = "Harry"
for i in s:
    print(i)


#4.for with else
l= [1,7,8] 

for item in l:
    print(item)

else:
    print("done") # this is printed when the loop exhausts!

# example 2

for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
    if x == 3:
        break
    else:
        print ("else block in loop")

# if loop gets exhauseted then it prints else statement;
# if it breaks in between , the else statement do not get printed as the above if condition get satisfied
     
print ("Out of loop")    