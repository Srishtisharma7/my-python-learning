# METHOD OVERRIDING

'''allows you to redefine a method in a derived class. The method in the derived class is said to override the method in the base class. 
When you create an instance of the derived class and call the overridden method, the version of the method in the derived class is executed, 
rather than the version in the base class.'''

class Shape:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def area(self):
      return self.x * self.y

class Circle(Shape):    # inherit other properties of class shape
    def __init__(self, radius):
      self.radius = radius
      super().__init__(radius, radius)       # super inheriting area function but wrong implementation as cicle area is not r * r

    def area(self):
        return 3.14 *  super().area()  # so instead we override the area function that allows you to redefine a method in a derived class
      
# rec = Shape(3, 5)
# print(rec.area())

c = Circle(5)
print(c.area())








# #OPERATOR OVERLOADING

class Number:
    def __init__(self, n):
        self.n = n                            # initialize the attribute n with a value.

    def __add__(self, num):
        return self.n + num.n  
    #[it is mandatory to do so]  self.n is the lhs operand and num.n is the rhs operand
    # The __add__ method is called when the + operator is used with objects of the Number class.

n = Number(1)
m = Number(2)

print(n + m)

# n + m:
# Calls n.__add__(m), passing n as self and m as num.
# Inside the __add__ method: self.n is 1 (from n) and num.n is 2 (from m).
# Returns 1 + 2 = 3. ie; the result


# example 2:

class Vector:
  def __init__(self, i, j, k):
    self.i = i
    self.j = j
    self.k = k

  def __str__(self):
    return f"{self.i}i + {self.j}j + {self.k}k"

  def __add__(self, x):      # without this function , cant add v1 and v2  , it will show error
    return Vector(self.i + x.i,  self.j+x.j, self.k+x.k) 
  
v1 = Vector(3, 5, 6)
print(v1)

v2 = Vector(1, 2, 9)
print(v2)

print(v1 + v2)
print(type(v1 + v2))



'''In Python, operators like +, -, *, etc., are designed to work with built-in data types.
Operator overloading allows us to define custom behavior for these operators when they are used with objects of user-defined classes.
This is achieved by implementing special methods (also called magic methods or dunder methods) like __add__, __sub__, etc., in a class.

Operation	             Expression	                   Magic Method                               Explanation

Addition	            p1 + p2	                      p1.__add__(p2)	                       Adds two objects.
Subtraction             p1 - p2	                      p1.__sub__(p2)	                       Subtracts p2 from p1.
Multiplication	        p1 * p2	                      p1.__mul__(p2)                           Multiplies two objects.
Division	            p1 / p2	                      p1.__truediv__(p2)                       Performs true division of two objects.
Floor Division	        p1 // p2	                  p1.__floordiv__(p2)	                   Performs floor division.
Modulo             	    p1 % p2                       p1.__mod__(p2)	                       Computes the remainder of division.
Power	                p1 ** p2	                  p1.__pow__(p2)	                       Raises p1 to the power of p2.
String Concatenation	str1 + str2	                  str1.__add__(str2)	                   Adds two strings.
'''





