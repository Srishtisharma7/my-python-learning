# The import string statement in Python imports the string module, which provides a collection of utilities and constants to work with strings. Here's an overview of what you can use from the string module:

# string.ascii_letters
# # Contains all the lowercase and uppercase ASCII letters:
# # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


# string.ascii_lowercase
# # Contains all the lowercase ASCII letters:
# 'abcdefghijklmnopqrstuvwxyz'


# string.ascii_uppercase
# # Contains all the uppercase ASCII letters:
# 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# string.digits
# # Contains all decimal digits:
# '0123456789'



# string.hexdigits
# # Contains all hexadecimal digits (lowercase and uppercase):
# '0123456789abcdefABCDEF'



# string.punctuation
# # Contains all printable punctuation characters:
# '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'




# string.printable
# # Contains all printable characters (digits, letters, punctuation, and whitespace):
# '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'



# string.whitespace
# # Contains all whitespace characters:
# ' \t\n\r\x0b\x0c'




# # Usage Examples:
# # Random String Generation:

import string
import random

# Generate a random string of 10 characters
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
print(random_string)  # Example output: 'A9bX2cDfG3'




# Removing Punctuation:

import string

text = "Hello, World!"
cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
print(cleaned_text)  # Output: 'Hello World'




# Validating a String:

import string

text = "123abc"
if all(char in string.ascii_letters + string.digits for char in text):
    print("String contains only letters and digits.")
else:
    print("String contains other characters.")



# The string module is lightweight and extremely useful for many string manipulation tasks, especially when combined with functions like random.choices, str.translate, and all.