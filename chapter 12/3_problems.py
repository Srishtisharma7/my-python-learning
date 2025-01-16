# 2. Write a program to input name, marks and phone number of a student and format it using the format function like below:
# “The name of the student is Harry, his marks are 72 and phone number is 99999888”

name = input("Enter name: ")
marks = int(input("Enter marks: "))
phone = int(input("Phone number: "))

s = "The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phone)

print(s)





# 3. A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.

table = [str(7*i) for i in range(1, 11)]
# str(7*i) converts each number to a string to enable joining later.

s = "\n".join(table)
print(s)
# ombines the elements of table into a single string separated by newline characters (\n).


# 4. Write a program to filter a list of numbers which are divisible by 5.

def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a  = [1,2,34234,53,6234235,64343, 65,754,45,55]

f = list(filter(divisible5, a))
print(f)

# alternate using lambda
a = [1, 2, 34234, 53, 6234235, 64343, 65, 754, 45, 55]

f = list(filter(lambda n: n % 5 == 0, a))
print(f)




# 5. Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce
l  = [111, 2, 65, 5553, 635, 65, 74, 45,55]


def greater(a, b):
    if (a>b):
        return a 
    return b

print(reduce(greater, l))

'''The reduce function applies the greater function to the list l.
It starts with the first two elements (111 and 2), compares them, and keeps the larger one.
It then compares this result with the next element in the list, continuing until all elements have been processed.
The result is the greatest number in the list.'''

print(max(l))    # alternate built in funcn to find max







# 7. Explore the ‘Flask’ module and create a web server using Flask & Python.
from flask import Flask

app = Flask(__name__) # Here, you're creating an instance of the Flask class. __name__ is passed to indicate the current module (in this case, the script file).
# this instance represents the web application.

@app.route("/")  
def hello_world():
    return "<p>Hello, World!</p>"

#the @app.route("/") decorator is used to define a route. The route "/" refers to the home page (or root URL) of the web application.
# When a user navigates to this route, the hello_world() function is executed, and it returns the string "<p>Hello, World!</p>", which is the response sent to the user's browser.

app.run()

# app.run() starts the Flask web server, which listens for incoming requests.
# By default, Flask runs on http://127.0.0.1:5000/, which is the local address of the web server. You can access this server by typing the URL in your web browser.
