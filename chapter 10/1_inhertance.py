'''Inheritance is a way of creating a new class from an existing class.
Syntax:
class Employee: # Base class
# Code
class Programmer(Employee): # Derived or child class'''

class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")

'''instead of copying methods we use inheritance to derive functions for multiple clasee and 
if we have to change something we just update into parent class , derived class will get updated simultaneoulsy '''

'''SINGLE INHERITANCE
Single inheritance is a type of inheritance where a class inherits properties and behaviors from a single parent class. 
This is the simplest and most common form of inheritance.'''


class Programmer(Employee):           # child(parent)
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
b = Programmer()

print(a.company, b.company)


# example 2

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")

d = Dog("Dog", "Doggerman")
d.make_sound()

a = Animal("Dog", "Bulldog")
a.make_sound()

'''The Dog class inherits all the attributes and behaviors of the Animal class, including the __init__ method and the make_sound method.Additionally, 
the Dog class has its own __init__ method that adds a new attribute for the breed of the dog, and it also overrides the make_sound method to specify the sound that a dog makes'''