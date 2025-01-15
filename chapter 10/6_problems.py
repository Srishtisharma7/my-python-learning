''' 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.'''

class TwoDVector:
    def __init__(self, i, j):     # constructor defined passing i and j 
        self.i = i
        self.j = j               # value passed through self
    
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j ")
        

class ThreeDVector(TwoDVector):         # class inherited from twoDvector
    def __init__(self, i, j, k):
        super().__init__(i, j)             # super gains the access for constructor of parent class as well so no need to pass i and j here as it already have
        self.k = k                        # just pass k in self here, i and j will be passed through the constructor of the parent class]

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")    # call all the vectors through self

a = TwoDVector(1, 2)             # object created a and b for both classes
a.show()
b = ThreeDVector(5, 2, 3)
b.show()
 
# outputs are : The vector is 1i + 2j 
#The vector is 5i + 2j + 3k 





'''2. Create a class 'Pets' from a class 'Animals' and further create a class 'Dog' from 'Pets'. Add a method 'bark' to class 'Dog'.'''

class Animals:
    pass 

class Pets(Animals):
    pass                             # class created but nothing to execute in them for now, but can be added in future

class Dog(Pets):

    @staticmethod                    # a read function only, so no need to pass the arguments
    def bark():
        print("Bow Bow!")


d = Dog()         # object created for class dog 

d.bark()          # and function called , outputs: Bow Bow!







'''3. Create a class 'Employee' and add salary and increment properties to it. Write a method 'salaryAfterIncrement' method with
a @property decorator with a setter which changes the value of increment based on the salary.'''
#property decorator and its setter are used to calculate and update an attribute dynamically in a Python class.

class Employee:
    salary = 234
    increment = 20          # properties added in the class
    
    @property
    def salaryAfterIncrement(self):                 # takes from the class self
        return (self.salary + self.salary * (self.increment/100))       
    
    #@property ka method will return us salary after increment 

    @salaryAfterIncrement.setter 
    def salaryAfterIncrement(self, salary): # salary passed is new salry after increment passed from above method , setter method used to get it
        self.increment =  ((salary/self.salary) -1)*100 
    
    #@setter ka method will now work on salary after increment and will take this and the old salary from self to return the increment



e = Employee()  # object created
print(e.salaryAfterIncrement)   #Getter: Calculates and prints the salary after increment (280.8).
e.salaryAfterIncrement = 280.8     # Setter: Updates `increment` based on the new salary value.
print(e.increment)  # = 20% Prints the updated increment (20.0).

'''
@property decorator:

Converts the method into a readable property.
Allows accessing salaryAfterIncrement as if it were an attribute (e.g., e.salaryAfterIncrement).

@<property_name>.setter decorator:

Defines how the property value is updated.
Allows setting salaryAfterIncrement dynamically (e.g., e.salaryAfterIncrement = 280.8).
When you assign a value to salaryAfterIncrement, the increment percentage is recalculated based on the new salary value.
Formula: increment = ((new_salary / base_salary) - 1) * 100.

If new_salary = 280.8 and base_salary = 234:
increment = ((280.8 / 234) - 1) * 100 = (1.2 - 1) * 100 = 20%

The increment is updated dynamically when salaryAfterIncrement is set.

'''







