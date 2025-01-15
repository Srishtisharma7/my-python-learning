'''CLASS METHOD'''
#the term "constructor" refers to a special type of method that is automatically executed when an object is created from a class. 
# The purpose of a constructor is to initialize the object's attributes, allowing the object to be fully functional and ready to use.
#However, there are times when you may want to create an object in a different way, or with different initial values, than what is provided
# by the default constructor. This is where class methods can be used as alternative constructors.

# A class method is a method which is bound to the class and not the object of the class.
# @classmethod decorator is used to create a class method.

class Employee:
    a = 1
    
    @classmethod                                               #instead of def(self), we use def (cls)  
    def show(cls):
        print(f"The class attribute of a is {cls.a}")           # to get class attribute of a =1 

e = Employee()
e.a = 45                   #instance attribute a =45 it gets printed always but we want to have class attribute so we use class method

e.show()

# The class attribute of a is 1 is the output , without @classmethod the output wud have been a = 45

'''method that creates instances of your class in a specific way. You could define a class method that creates the instance and
returns it to the caller. Another common use case is to provide alternative constructors for your class'''

class Employee:
  company = "Apple"
  def show(self):
    print(f"The name is {self.name} and company is {self.company}")

  @classmethod
  def changeCompany(cls, newCompany):        # cls is just a keyword or class name same like employee jiske through instance access hoga
    cls.company = newCompany                   # without classmethod, it acts as a instance


e1 = Employee()
e1.name = "Harry"
e1.show()                        # the name is Harry and company is Apple
e1.changeCompany("Tesla")
e1.show()                            # The name is Harry and company is Tesla
print(Employee.company)          # tesla
 

# class methods as alternate constructors

# if data is given in different data formats like ("harry-20000") or ("john,1500") instead of normal arguments passing like ("harry" , 20000)
# we define a class method that makes our code cleaner and derive the arguments from different data formats by string slicing and typecasting as per need

class Employee:
  def __init__(self, name, salary):
    self.name = name 
    self.salary = salary
    
  @classmethod
  def fromStr(cls, string):
    return cls(string.split("-")[0], int(string.split("-")[1]))      # here we slicing string by - values and int typecasting the salary value at 1 index
    # returning the arguments as well to the classmethod

e1 = Employee("Harry", 12000)     # a normal argument
print(e1.name)
print(e1.salary) 

string = "John-12000"        # argument to be derived from thi string
e2 = Employee.fromStr(string)    # take arguments fromstr classmethod
print(e2.name)
print(e2.salary)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod        # diff classmethods defined for different dataformats or functions , act as constructor as initializes the arguments and create instances
    def from_string(cls, string):
        name, age = string.split(',')       # here string slicing , values pe and typecasting also
        return cls(name, int(age))

person = Person.from_string("John Doe, 30")
print(person.name, person.age)





'''PROPERTY DECORATORS'''


class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property 
    def name(self):
        return f"{self.fname} {self.lname}" #reurns f string for first and last name
    
#The @property decorator allows you to define a method (name) that acts like a read-only attribute. (basically for printing)
#When e.name is accessed, it returns the full name by combining the fname and lname attributes.
    
    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0]        #indexing 0 value wud be fname and index 1 wali wud be lname
        self.lname = value.split(" ")[1]

# The @<property_name>.setter decorator allows the property to be modified.
# Here, when e.name = "Harry Khan" is called:
# It splits the value "Harry Khan" into fname = "Harry" and lname = "Khan", setting them as attributes of the instance


e = Employee()         # Creates an instance e of the Employee class.
e.a = 45               # Assigns a new value (45) to the instance attribute a. Note that this does not change the class attribute Employee.a.

e.name = "Harry Khan"     # This calls the @name.setter, splitting "Harry Khan" and assigning:  e.fname = "Harry" , e.lname = "Khan"
print(e.fname, e.lname)    # Outputs: Harry Khan

e.show()    #Calls the show method, which accesses the class attribute a (still 1 because e.a = 45 only modified the instance attribute).




