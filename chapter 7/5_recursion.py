# Recursion is a function which calls itself.
# It is used to directly use a mathematical formula as function.
'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1                            [3 x factorial 2]
factorial(4) = 4 X 3 X 2 X 1         [4 x factorial 3, in similar way ,if we ask factorial of 5 , it resolves it into n * factorial(n-1)]
factorial(5) = 5 X 4 X 3 X 2 X 1
factorial(n) = n X n-1 X......3 X 2 X 1
factorial(n) = n * factorial(n-1)
'''

# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1


def factorial(n):                #function defined to get factorial of a number
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)              # keep resolving till x 2 x 1...


n = int(input("Enter a number: "))
print(f"The factorial of this number is: {factorial(n)}")

# The programmer needs to be extremely careful while working with recursion to ensure that the function doesn’t infinitely keep calling itself.
# Recursion is sometimes the most direct way to code an algorithm.


# Write a program to print the Fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Input: number of terms to display
num_terms = int(input("Enter the number of terms: "))

print("Fibonacci sequence:")
for i in range(num_terms):
    print(fibonacci(i), end=" ")
