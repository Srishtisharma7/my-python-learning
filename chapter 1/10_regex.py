'''Regular expressions, or "regex" for short, are a powerful tool for working with strings and text data in Python. They allow you to 
match and manipulate strings based on patterns, making it easy to perform complex string operations with just a few lines of code.'''


'''The “re” module is composed of five functions known as:

findall: It finds all searches for matches and prints resultant in the form of a list.

search: It works the same as a findall, but the resultant is a matched object if any is found.

split: The split function splits the string from every matched into two new strings.

sub: The sub-function works exactly like a replace function in notepad or MS Word. It replaces the original word with a word of our choice.

finditer: The finditer yields an iterator as a resultant with all the objects that match the one we sent it) finditer supports more attributes 
than any other function defined above. It also provides more details related to the matched object. So, most of the examples we are going to see 
next will contain a finditer function in them.'''

# Use of “^”:-

'''We use the” ^” symbol to check whether the string is starting from the keyword we wrote after ^ or not. For example, if a string starts 
from CodeWithHarry and we are searching the keyword using ^CodeWithHarry with finditer, it will return us whether our string is starting 
from the searched keyword or not. The same is the case for $ sign. It will check whether our string is ending with the specific keyword or not.'''


# Use of “|”:-

'''We can also use a unique character “|” to use more than one condition, so if we use it for the above case, then it will check whether the string 
starts or ends with CodeWithHarry.Now we will move on to special sequences. We will see a few special sequences in this tutorial, and you can have a 
look at the list of these sequences at the end of the tutorial description for further practice. '''


''' There are many metacharacters supported by the re module. Some characters with their working are the following:'''

# ‘.’: Matches any single character except newline
# ‘$’: Anchors a match at the end of a string
# ‘*’: Matches zero or more repetitions
# ‘+':Matches one or more repetitions
# ‘{}’: Matches an explicitly specified number of repetitions
# ‘[]’: Specifies a character class or  A set of characters
# \ Signals a special sequence (can also be used to escape special characters)
# + One or more occurrences
# () Capture and group
# Special Sequences
# \A Returns a match if the specified characters are at the beginning of the string
# \b Returns a match where the specified characters are at the beginning or at the end of a word r” ain\b.”
# \B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word

# \d Returns a match where the string contains digits (numbers from 0-9)
# \D Returns a match where the string DOES NOT contain digits
# \s Returns a match where the string contains a white space character
# \S Returns a match where the string DOES NOT contain a white space character
# \w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
# \W Returns a match where the string DOES NOT contain any word characters
# \Z Returns a match if the specified characters are at the end of the string



import re

# https://regexr.com/     visit to learn more , along with official documentations of python docx
import re

pattern = r"[A-Z]+yclone"         # r means raw string , not evaluate pescape sequence characters , just match with pure pattern given

text = '''Cyclone Dumazile was a strong tropical cyclone in the South-West Indian Ocean that affected Madagascar and Réunion in 
early March 2018. Dumazile originated from a cyclone Dyclone low-pressure area that formed near Agaléga on 27 February. '''

match = re.search(pattern, text)
print(match)

# <re.Match object; span=(0, 7), match='Cyclone'>  (output : none if no match)

# matches = re.finditer(pattern, text)
# for match in matches:
#   print(match.span()) 
#   print(text[match.span()[0]: match.span()[1]])



# Searching for a pattern in re using re.search() Method
# re.search() method either returns None (if the pattern doesn’t match), or a re.MatchObject that contains information about the matching 
# part of the string. This method stops after the first match, so this is best suited for testing a regular expression more than extracting data. 
# We can use re.search method like this to search for a pattern in regular expression:

# Define a regular expression pattern
pattern = r"expression"

# Match the pattern against a string
text = "Hello, world!"

match = re.search(pattern, text)

if match:
    print("Match found!")
else:
    print("Match not found.")


# Searching for a pattern in re using re.findall() Method
# You can also use the re.findall function to find all occurrences of the pattern in a string:

import re
pattern = r"expression"
text = "The cat is in the hat."

matches = re.findall(pattern, text)

print(matches)
# Output: ['cat', 'hat']


# Replacing a pattern
# The following example shows how to replace a pattern in a string:

import re
pattern = r"[a-z]+at"
text = "The cat is in the hat."

matches = re.findall(pattern, text)

print(matches)
# Output: ['cat', 'hat']

new_text = re.sub(pattern, "dog", text)

print(new_text)
# Output: "The dog is in the dog."


# Extracting information from a string
# The following example shows how to extract information from a string using regular expressions:

import re

text = "The email address is example@example.com."

pattern = r"\w+@\w+\.\w+"

match = re.search(pattern, text)

if match:
    email = match.group()
    print(email)
# Output: example@example.com