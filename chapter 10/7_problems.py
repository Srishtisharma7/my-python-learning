'''4. Write a class 'Complex' to represent complex numbers, along with overloaded operators '+' and '*' which adds and multiplies them.'''

class Complex:
    def __init__(self, r, i):    #The constructor initializes the real (r) and imaginary (i) parts of one complex number.
        self.r = r
        self.i = i
# ek no. self se , ek c2 another complex no.
#c1 ka real and imaginary part self se liya jayega , or c2 ka c2 k through pass hoga and access

    def __add__(self, c2):                       
        return Complex(self.r + c2.r, self.i + c2.i)
    
#this _add_ Allows the + operator to add two Complex objects. 
# self refers to left operand and c2 refers to right operand and add the real and imaginary parts
# and then returns a new Complex object representing the sum.


    def __mul__(self, c2):             # overloading the * operator
        real_part = self.r * c2.r - self.i * c2.i
        imag_part = self.r * c2.i + self.i * c2.r
        return Complex(real_part, imag_part)
    
# eg: (1+2i)x(3+4i):
# real = (1x3) - (2x4) = 3-8 = -5
# imaginary = (1x4) + (2x3) = 10
# result = -5 + 10i

    def __str__(self):           # Defines how a Complex object is displayed as a string.
        return f"{self.r} + {self.i}i"
       

c1 = Complex(1, 2)        # Represents 1 + 2i
c2 = Complex(3, 4)        # Represents 3 + 4i
print(c1 + c2)            # Calls c1.__add__(c2)
print(c1*c2)              # Calls c1.__mul__(c2)









'''5. Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.'''

class Vector:          # Initializes the vector with its components x,y and z

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
# ek no. self se , ek other no. pass hoga constructor me to let the access of its n vectors

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)   # vectorize the result
        return result
    
# self is lhs operand and other is rhs operand or no. , adds the corresponding component of two vectors
# like (x1 + x2) , (y1+y2), then returns a new vector object as result like (3,4,5)

    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result

# same here, dot product formula is applied and return is scalar (not vector) like 32

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

# f string nsures that the vector components are dynamically included in the string representation of the object
# f string allows you to include the actual values of self.x, self.y, and self.z directly within the string.[are efficient and improves readability]
# if not f string , use string concatenation but its less preffered
# Defines how the vector is displayed when printed or converted to a string.
#A vector with x = 5 , y = 7 and z = 9 is displayed as "Vector(5, 7, 9)"


# Test the implementation
v1 = Vector(1, 2, 3)     # v1 object created explicitly
v2 = Vector(4, 5, 6)     # v2 object
v3 = Vector(7, 8, 9)  # Same dimension vector

print(v1 + v2)  # Output: Vector(5, 7, 9)  [returns a new vector object implicitly]
print(v1 * v2)  # Output: 32

print(v1 + v3)  # Output: Vector(8, 10, 12)
print(v1 * v3)  # Output: 50





''' 6. Write __str__() method to print the vector as follows:
7i + 8j +10k [Assume vector of dimension 3 for this problem.]'''

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"  #Customizes the string representation of the vector. no need to vectorize now

# Test the implementation
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)  # Same dimension vector

print(v1 + v2)  # Output: Vector(5, 7, 9)
print(v1 * v2)  # Output: 32

print(v1 + v3)  # Output: Vector(8, 10, 12)
print(v1 * v3)  # Output: 50





'''7. Override the __len__() method on vector of problem 5 to display the dimension of the vector.'''

class Vector:
    def __init__(self, l): 
        self.l = l

# initializes a Vector object with a list l, which represents the vector's components.
    
    def __len__(self):
        return len(self.l)   # returns length of list l, which corresponds to vector dimension
    
# Overrides Python's built-in len() function.
# Returns the length of the list l, which corresponds to the dimension of the vector.

# Test the implementation
v1 = Vector([1, 2, 3]) 
print(len(v1))

v2 = Vector([4, 5])       # A 2-dimensional vector,  here vector is passed as list
v3 = Vector([7, 8, 9, 10]) # A 4-dimensional vector

print(len(v2))  # Output: 2
print(len(v3))  # Output: 4

#why lists? = Best for simplicity and flexibility.
'''
Tuple: If immutability is needed.
Dictionary: If named components are required 
Numpy Array: For advanced mathematical operations

instead this code can work also apart from storing it in lists, tuples , dictionaries an then returning their lengths
'''

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __len__(self):
        return 3  # Hardcoded for a 3D vector

v = Vector(1, 2, 3)
print(len(v))  # Output: 3

# This approach only works for fixed-dimension vectors (e.g., 3D).
# Not flexible for higher or lower-dimensional vectors.
