'''SELF PARAMETER: or 'self argument'
self refers to the instance of the class. It is automatically passed with a function call from an object.'''

# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It must be provided as the extra parameter inside the method definition.

'''CONSTRUCTOR: or __init__()
It is a special method which is first run as soon as the object is created.
It takes self argument and can also take further arguments
'''

# Constructor is a special method in a class used to create and initialize an object of a class. 
# initialize or assign values to the data members of that class. It cannot return any value other than None.

class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def getInfo(self):   # mentioned self
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod   
    def greet():
        print("Good morning")
 # Sometimes we need a function that does not use the self-parameter.like greet just says good morning, 
 # there is no need to pass entire object though self, as we do not need anything from the object (name,language or salary)
 # but then it shows error so to rectify it ,we use staticmethod

harry = Employee()
# harry.language = "JavaScript" # This is an instance attribute
harry.greet()
harry.getInfo() #gets converted into
# Employee.getInfo(harry)   >  so here , harry is passed as arguement as self 

# Static methods in Python are methods that belong to a class rather than an instance of the class. Another example:

class Math:
  def __init__(self, num):
    self.num = num

  def addtonum(self, n):    #here self needed
    self.num = self.num +n
    
  @staticmethod     # no self needed
  def add(a, b):
      return a + b

# result = Math.add(1, 2)
# print(result) # Output: 3
a = Math(5)
print(a.num)
a.addtonum(6)  # take self
print(a.num)

print(Math.add(7, 2))     # static , no self take its own arguments like a normal function

# In this example, the add method is a static method of the Math class. It takes two parameters a and b and returns their sum. 
# The method can be called on the class itself, without the need to create an instance of the class.
