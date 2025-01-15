# Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"         #class attribute , same for all
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = Programmer("Harry", 1200000, 245001)
print(p.name, p.salary, p.pin, p.company)
r = Programmer("Rohan", 1200000, 245001)
print(r.name, r.salary, r.pin, r.company)





# 2. Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator:
    def __init__(self, n):
        self.n = n               #Here, n is passed when creating the object (e.g., Calculator(4)), and it is stored in the instance variable self.n.
    
    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot is {self.n**(1/2)}")       # power ke liye we do **1/2

a = Calculator(4)   # n ki value passed also [This creates an object a of the Calculator class, passing 4 as the value for n.]
a.square()         #constructor called 
a.cube()
a.squareroot()
#Calls the square, cube, and squareroot methods, performing the respective calculations and printing the results.





# 3. Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’
# Does this change the class attribute?

class Demo:
    a = 4    # class attribute a

o = Demo()               # set object o here for class demo
print(o.a)              # Prints the class attribute because instance attribute is not present = 4
o.a = 0                  # Instance attribute is set
print(o.a)               # Prints the instance attribute because instance attribute is preferred = 0 , but c.a remains same
print(Demo.a)              # Prints the class attribute = 4 , so class attribute do not change





# 4. Add a static method in problem 2, to greet the user with hello.

class Calculator:
    def __init__(self, n):
        self.n = n 
    
    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot is {self.n**1/2}")
    
    @staticmethod    # no need to use self or object
    def hello():
        print("Hello there!")

a = Calculator(4)
a.hello()
a.square()
a.cube()
a.squareroot()





# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

from random import randint # so we use randint directly instead of , random.randit if we just import random

class Train:

    def __init__(self, trainNo):    #defined a init constructor which gets called every time for every object created
        self.trainNo = trainNo    # train no. is instance attribute for the class train , so passed every time for the obect

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}") 
# train no. no alag se need to be passed, it gets from self value

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time") 

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")  # randint generate random no. for fare within range


t = Train(12399)   # object created and init called with train no. as self
t.book("Nagpur", "Delhi")       # pass required parameters
t.getStatus()   # gets from self
t.getFare("Nagpur", "Delhi")





# 6. Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.

from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo
# just change at both places 
    def book(harry, fro, to):
        print(f"Ticket is booked in train no: {harry.trainNo} from {fro} to {to}") 

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time") 

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")  


t = Train(12399)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")

#no effect , output comes same and correct but self is used for better readability
