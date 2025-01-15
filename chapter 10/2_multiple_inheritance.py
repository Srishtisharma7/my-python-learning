'''MULTIPLE INHERITANCE'''
# When a class can be derived from more than one base class this type of inheritance is called multiple inheritances. 
# In multiple inheritances, all the features of the base classes are inherited into the derived class.

class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")
     


class Programmer(Employee, Coder):   # one class gets properties of two classes ; multiple inheritance
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")


a = Employee()
b = Programmer()   #object created for both classes

b.show()   #from employee class
b.printLanguages()   #from programmer class
b.showLanguage()      # from coder class

# output for all the functions :
# the name of the Employee is Default name and the company is ITC Infotech
# Out of all the languages here is your language: Python
# The name is ITC Infotech and he is good with Python languag



# example 2:

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")
        
class Mammal:
    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color
        
class Dog(Animal, Mammal):
    def __init__(self, name, breed, fur_color):
        Animal.__init__(self, name, species="Dog")
        Mammal.__init__(self, name, fur_color)
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")
# the Dog class inherits from both the Animal and Mammal classes, so it can use attributes and methods from both parent classes.


# example 3:

class Employee:
  def __init__(self, name):
    self.name = name
  def show(self):
    print(f"The name is {self.name}")

class Dancer:
  def __init__(self, dance):
    self.dance = dance

  def show(self):
    print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
  def __init__(self, dance, name):
    self.dance = dance
    self.name = name

o  = DancerEmployee("Kathak", "Shivani")
print(o.name)
print(o.dance)
o.show() 
print(DancerEmployee.mro())

# <class '__main__.DancerEmployee'>, <class '__main__.Employee'>, <class '__main__.Dancer'>, <class 'object'>]

# MRO defines the sequence in which Python looks for methods and attributes when they are accessed.
# For example, if you call a method on an object, Python checks the class of the object first, and if the method is not found, it searches the parent classes in the order defined by MRO.
# the show() method in DancerEmployee first looks in Employee (since it's before Dancer in the MRO). This predictable order ensures clarity and avoids confusion in complex inheritance hierarchies
# Avoids conflicts in multiple inheritance: MRO prevents potential issues like the "diamond problem," where a method is inherited from multiple classes        










'''MULTILEVEL INHERITANCE'''
# In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class. 
# This is similar to a relationship representing a child and a grandfather.

class Employee:
    a = 1 

class Programmer(Employee):
    b = 2 

class Manager(Programmer):
    c = 3

'''The Manager class inherits from Programmer, so it will have access to a (from Employee), b (from Programmer), and c (its own attribute).'''


o = Employee()
print(o.a) # Prints the a attribute = 1
# print(o.b) # Shows an error as there is no b attribute in Employee class its the main parents class

o = Programmer()
print(o.a, o.b)
# 1,2

o = Manager()
print(o.a, o.b, o.c)   # can access all classes attributes , prints 1,2,3



# example :

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")
        
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color
        
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")

o = Dog("tommy", "Black")
o.show_details()
o = GoldenRetriever("tommy", "Black")     # breed default printed
o.show_details()
print(GoldenRetriever.mro())        

'''the GoldenRetriever object has access to all the attributes and methods of the Animal and Dog classes, and, it has also added its own unique 
attributes and methods. This is a powerful feature of multilevel inheritance, as it allows you to create more complex and intricate classes by building upon existing ones.'''       

# it allows you to reuse code and avoid repeating the same logic multiple times. This can lead to better maintainability and readability of your code, as you can abstract away
# complex logic into base classes and build upon them.








'''HIERARCHICAL INHERITANCE'''
# When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance.
#  In this program, we have a parent (base) class and two child (derived) classes.

class Parent:
    def func1(self):
        print("This function is in parent class.")

class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")
      
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")
 
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()



# example 2 :

class Animal:
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print("Name:", self.name)

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print("Species: Dog")
        print("Breed:", self.breed)

class Cat(Animal):
    def __init__(self, name, color):
        Animal.__init__(self, name)
        self.color = color

    def show_details(self):
        Animal.show_details(self)
        print("Species: Cat")
        print("Color:", self.color)

dog = Dog("Max", "Golden Retriever")
dog.show_details()
cat = Cat("Luna", "Black")
cat.show_details()        
#the Dog and Cat classes have inherited the attributes and methods of the Animal class, and have also added their own unique attributes and methods.

# in Python, hybrid inheritance can be implemented by creating a class hierarchy, in which a base class is inherited by 
# multiple derived classes, and one of the derived classes is further inherited by a sub-derived class.

class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def show_details(self):
    print("Name:", self.name)
    print("Age:", self.age)
    
class Person(Human):
  def __init__(self, name, age, address):
    Human.__init__(self, name, age)
    self.address = address
    
  def show_details(self):
    Human.show_details(self)
    print("Address:", self.address)
    
class Program:
  def __init__(self, program_name, duration):
    self.program_name = program_name
    self.duration = duration
    
  def show_details(self):
    print("Program Name:", self.program_name)
    print("Duration:", self.duration)
    
class Student(Person):
  def __init__(self, name, age, address, program):
    Person.__init__(self, name, age, address)
    self.program = program
    
  def show_details(self):
    Person.show_details(self)
    self.program.show_details()

program = Program("Computer Science", 4)
student = Student("John Doe", 25, "123 Main St.", program)
student.show_details()

'''the Student class inherits from the Person class, which in turn inherits from the Human class. The Student class also has an 
association with the Program class. This is an example of Hybrid Inheritance in action, as it uses both Single Inheritance and Association 
to achieve the desired inheritance structure'''