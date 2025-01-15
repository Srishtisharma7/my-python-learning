class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1 

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2 

class Manager(Programmer):
    def __init__(self):
        super().__init__()                      # super() method is used to access the methods or constructors of a super class in the derived class.
        print("Constructor of Manager")
    c = 3

# o = Employee()
# print(o.a) # Prints the a attribute or constructor of a only

# o = Programmer()
# print(o.a, o.b) prints constructor of b only


o = Manager()
print(o.a, o.b, o.c)

# output :Constructor of Programmer
#         Constructor of Manager (manager me super init lgaya to it access constructor of its parents class also ie; programmer
#         1 2 3

# with super , it access constructors or functions of a super or a parent class



"""Access modifiers"""   # (in python no concept as such , just conventions for private modifiers )

# All the variables and methods (member functions) in python are by default public. 

'''
In Python, there is no strict concept of "private" access modifiers like in some other programming languages. However, a convention has been established to 
indicate that a variable or method should be considered private by prefixing its name with a double underscore (__). This is known as a "weak internal use
indicator" and it is a convention only, not a strict rule. Code outside the class can still access these "private" variables and methods, but it is generally 
understood that they should not be accessed or modified.


"protected" is used to describe a member (i.e., a method or attribute) of a class that is intended to be accessed only by the class itself and its subclasses.
In Python, the convention for indicating that a member is protected is to prefix its name with a single underscore (_). For example, if a class has a method called _my_method, 
it is indicating that the method should only be accessed by the class itself and its subclasses.

It's important to note that the single underscore is just a naming convention, and does not actually provide any protection or restrict access to the member. 
The syntax we follow to make any variable protected is to write variable name followed by a single underscore (_) ie. _varName.
'''

class Student: 
    def __init__(self, age, name): 
        self.__age = age      # An indication of private variable (age) using double underscore
        
        def __funName(self):  # An indication of private function
            self.y = 34
            print(self.y)

class Subject(Student):
    pass

obj = Student(21,"Harry")
obj1 = Subject

# calling by object of class Student
# print(obj.__age)
# print(obj.__funName())
print(obj._Student__age)              # this will run after little mangling [_classname__private variable or function]
# print(obj._Student__funName())

# output : AttributeError: 'student' object has no attribute '__age'
# AttributeError: 'student' object has no method '__funName()'
# Private members of a class cannot be accessed or inherited outside of class. 
# If we try to access or to inherit the properties of private members to child class (derived class). Then it will show the error

'''so we use name mangling'''

# Name mangling in Python is a technique used to protect class-private and superclass-private attributes from being accidentally overwritten by subclasses.
# Names of class-private and superclass-private attributes are transformed by the addition of a single leading underscore and a double leading underscore respectively.

class MyClass:
    def __init__(self):
        self._nonmangled_attribute = "I am a nonmangled attribute"
        self.__mangled_attribute = "I am a mangled attribute"

my_object = MyClass()
# use a single leading underscore
print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
# print(my_object.__mangled_attribute) # Throws an AttributeError
print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute