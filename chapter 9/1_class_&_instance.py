'''
A class is a blueprint for creating object.
An object is an instantiation of a class. When class is defined, a template (info) is defined. Memory is allocated only after object instantiation.

CLASS ATTRIBUTES:
An attribute that belongs to the class rather than a particular object.Class variables are defined at the class level and are shared among all instances 
of the class. They are defined outside of any method and are usually used to store information that is common to all instances of the class. For example, 
a class variable can be used to store the number of instances of a class that have been created.

INSTANCE ATTRIBUTES:
An attribute that belongs to the Instance (object).Instance variables are defined at the instance level and are unique to each instance of the class. 
They are defined inside the init method and are usually used to store information that is specific to each instance of the class. For example, 
an instance variable can be used to store the name of an employee in a class that represents an employee
obj1 = Details() 

class Details:
    name = "Rohan"
    age = 20

obj1 = Details()
print(obj1.name)
print(obj1.age)'''



class Employee: 
    language = "Py" # This is a class attribute , shared by all
    salary = 1200000


harry = Employee()
harry.name = "Harry" # This is an instance or object attribute
print(harry.name, harry.language, harry.salary)

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name, rohan.salary, rohan.language)

# Here , name is instance attribute and salary and language are class attributes as they directly belong to the class
# output : Harry Py 1200000
# Rohan Roro Robinson 1200000 Py


class Person:
  name = "Harry"
  occupation = "Software Developer"
  networth = 10
  def info(self):
    print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
c = Person()

a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Nitika"
b.occupation = "HR"

# print(a.name, a.occupation)
a.info()
b.info()
c.info()



'''Instance vs class attribute
Instance attributes, take preference over class attributes during assignment & retrieval.
'''
class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000


harry = Employee()
harry.language = "JavaScript" # This is an instance attribute, more preferred 
print(harry.language, harry.salary)
 
# output : JavaScript 1200000 


'''Example 2'''

class Employee:
  companyName = "Apple"       # class variable Shared across all instances, initially set to "Apple".
  noOfEmployees = 0
  def __init__(self, name):
    self.name = name        # store name of employee
    self.raise_amount = 0.02      # Represents the raise percentage for the specific employee, initialized to 0.02. 
    Employee.noOfEmployees +=1  #Tracks the total number of employees. It's incremented every time a new instance is created.
  def showDetails(self):
    print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

# Employee.showDetails(emp1)
emp1 = Employee("Harry")
emp1.raise_amount = 0.3
emp1.companyName = "Apple India"  # preferred instance , do not affect class variable
emp1.showDetails()
Employee.companyName = "Google"
print(Employee.companyName)        # outputs "Google" since the class-level companyName was updated.


emp2 = Employee("Rohan")
emp2.companyName = "Nestle"
emp2.showDetails()