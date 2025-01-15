'''Constructor'''


class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

# When the constructor accepts arguments along with self, it is known as parameterized constructor.
# These arguments can be used inside the class to assign the values to the data members.

    def __init__(self, name, salary, language): # in python methods which _starts with are dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")


harry = Employee("Harry", 1300000, "JavaScript") 
# harry.name = "Harry"
print(harry.name, harry.salary, harry.language)

rohan = Employee("Rohan", 120000, "Java") 
print(rohan.name,rohan.salary,rohan.language)
# an object is created , so dunder or constructor is called here too or whenever an object is created always always invoked


# When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor.
class Details:
  def __init__(self):
    print("animal Crab belongs to Crustaceans group")
obj1=Details()



'''Dunder methods'''

'''Magic methods, also known as “dunders” from the double underscores surrounding their names, are powerful tools that allow you to customize the behaviour of your classes.
 They are used to implement special methods such as the addition, subtraction and comparison operators, as well as some more advanced techniques like descriptors and properties.'''

# __init__method or constructor = special method that is automatically invoked when you create a new instance of a class. This method is responsible for setting up the object’s initial state, 
# and it is where you would typically define any instance variables that you need.

# The str and repr methods are both used to convert an object to a string representation. The str method is used when you want to print out an object,
#  while the repr method is used when you want to get a string representation of an object that can be used to recreate the object.

#__len__ method = The len method is used to get the length of an object. This is useful when you want to be able to find the size of a data structure, 
# such as a list or dictionary.

#__call__ method : The call method is used to make an object callable, meaning that you can pass it as a parameter to a function and it will be executed when the function is called. 
# This is an incredibly powerful tool that allows you to create objects that behave like functions.

class Employee:

  def __init__(self, name):
    self.name = name

  def __len__(self):
    i = 0
    for c in self.name:
      i = i + 1
    return i

  def __str__(self):
    return f"The name of the employee is {self.name} str"
    
  def __repr__(self):
    return f"Employee('{self.name}')"

  def __call__(self):
    print("Hey I am good")

e = Employee("Harry")
print(str(e))
print(repr(e))
print(e.name)
print(len(e))
e()

# The name of the employee is Harry str
# Employee('Harry')
# Harry
# 5
# Hey I am good


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __len__(self):
        return len(self.title)

book = Book("1984", "George Orwell")
print(str(book))  # Output: '1984' by George Orwell
print(len(book))  # Output: 4