name = "harry"

#print length of the string
print(len(name))

#String.endswith("rry") – This function_ tells whether the variable string ends with the string "rry" or not. 
# If string is "harry", it returns true for "rry" since Harry ends with rry
print(name.endswith("rry"))                 #true
print(name.endswith("rryii"))               #false


print(name.startswith("ha"))                #return true 
print(name.startswith("Ha"))                #return false since function is case sensitive

#capitalize only the first character of a given string
print(name.capitalize())                     #harry is > Harry is

# string.count("c") : counts the total number of occurrences of any character.
str = "harry"
count = str.count("r")
print(count)                # Output: 2

#string.find(word) – This function finds a word and returns the index of its first occurrence of that word in the string.
index = str.find("rr")
print(index) # Output: 2 at 2nd index (012) it occurs first

#string.replace (old word, new word ) – This function replace the old word with new word in the entire string at every occurence
replaced_string = str.replace("r", "l")
print(replaced_string) # Output: "hally"


# casefold(): Converts the string to lowercase (more aggressive than lower()).
# lower(): Converts all characters to lowercase.
# upper(): Converts all characters to uppercase.
# swapcase(): Swaps uppercase to lowercase and vice versa.
# title(): Converts the first character of each word to uppercase.

# isalnum(): Returns True if all characters are alphanumeric.
# The isalnum0 method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.

# isalpha(A-z, a-z.): Returns True if all characters are alphabetic.
# isdigit(): Returns True if all characters are digits.
# isdecimal(): Returns True if all characters are decimal digits.
# isnumeric(): Returns True if all characters are numeric.
# isidentifier(): Checks if the string is a valid Python identifier.
# islower(): Returns True if all characters are lowercase.
# isupper(): Returns True if all characters are uppercase.
# istitle(): Returns True if the string is in title case. (returns True only if the first letter of each word of the string is capitalized, else it returns False.)
# isspace(): Returns True if all characters are whitespace.   through tabs or "     " 
# isprintable0: The isprintable method returns True if all the values within the given string are printable, if not, then return False.(\n not printable , dont get printed)


"""strip(chars): Removes leading and trailing characters (default is whitespace).
lstrip(chars): Removes leading characters.
rstrip(chars): Removes trailing characters.
replace(old, new, count): Replaces occurrences of a substring with another.
join(iterable): Joins elements of an iterable with the string as a separator.
split(sep, maxsplit): Splits the string into a list.
rsplit(sep, maxsplit): Splits from the right into a list.
splitlines(keepends): Splits the string into a list at line breaks.
partition(sep): Splits the string into three parts: before, separator, and after.
rpartition(sep): Splits the string from the right into three parts.
expandtabs(tabsize): Expands tabs in the string to spaces.
format(*args, **kwargs): Formats the string using placeholders.
format_map(mapping): Similar to format() but uses a mapping.
maketrans(): Creates a translation table for translate().
translate(table): Translates the string using a translation table."""

# Encoding
# encode(encoding, errors): Encodes the string into bytes.
# decode(encoding, errors) (when applied to bytes): Decodes bytes to a string.

# Other Utility Functions

""" startswith(prefix, start, end): Checks if the string starts with a prefix.
endswith(suffix, start, end): Checks if the string ends with a suffix.
len(string) (built-in): Returns the length of the string.
ord(char) (built-in): Returns the Unicode code of a character.
chr(code) (built-in): Converts a Unicode code to a character."""


# Strings are immutable
a = "!!!Harry!! !!!!!!!!! Harry"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))           # rstrip(chars): Removes trailing characters.
print(a.replace("Harry", "John"))
print(a.split(" "))       #split(sep, maxsplit): Splits the string into a list.  breaks string('apple me an') = apple , me , an(into list)
blogHeading = "introduction tO jS"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(len(str1))                            # 25 len of string
print(len(str1.center(50)))                 # aligns to the centre leaving first 25 spaces total 50 len of string
print(a.count("Harry"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh"))
# print(str1.index("ishh")) returns -1
# The index method searches for the first occurrence of the given value and returns the index where it is present. 
# If given value is absent from the string then it raise an exception.(find) does not raise exception

str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
print(str1.swapcase()) 
 #pYTHON IS A iNTERPRETED lANGUAGE

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())
# His Name Is Dan. Dan Is An Honest Man.