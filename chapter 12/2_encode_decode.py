# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

import random
import string


def random_chars(n=3):
    """Generate `n` random characters."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

# string.ascii_letters : Contains all the lowercase and uppercase ASCII letters: a-z and A-Z
# string.digits : contains all digits 0 to 9
# k = n , Specifies the number of random elements to pick. The value of n is passed as an argument to the function.
# so the function generates 3 random no. (letter or digits) as our need and join them without space as ""


st = input("Enter message : ")                # Takes the input message from the user as a string.
words = st.split(" ")                       # Splits the input string into a list of words using space as a delimiter." "

coding = input("1 for Coding or 0 for Decoding : " )

coding = True if (coding=="1") else False

       
print(coding)
if(coding):
  nwords = []     # empty string
  for word in words:
    if(len(word)>=3):
      random_prefix = random_chars()
      random_suffix = random_chars()
      
      stnew = random_prefix + word[1:] + word[0] + random_suffix        # takes word from 1 index to end and then add the 0th index element at last and concatenate with r1 and r2
      nwords.append(stnew)                # Append this transformed word to the nwords empty list:
    else:
      nwords.append(word[::-1])             # reverses the string
  print(" ".join(nwords))               # Finally, joins the list into a single string and prints it with space given

# word[1:]: This takes all characters of the word except the first one.
# Example: For "hello", word[1:] gives "ello".
# word[0]: This takes the first character of the word.
# Example: For "hello", word[0] gives "h".

#  sequence[start:stop:step] for reversing a string
# [::-1], the start and stop are omitted, and the step is set to -1, so the sequence is reversed. +1 step to move in forward
# common use cases is_palindrome = word == word[::-1]
# print(is_palindrome)  # Output: True

else:
  nwords = []
  for word in words:
    if(len(word)>=3):  
      stnew = word[3:-3]                   # Remove 3 characters from the start and end
      stnew = stnew[-1] + stnew[:-1]       # Rotates the string by moving its last character to the beginning.
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])        # else reverse back fo to of
  print(" ".join(nwords))

# stnew = word[3:-3]
# This extracts a slice of the string word starting from the 4th character (index 3) up to (but not including) the 3rd-to-last character (index -3).ie; [actually the last 4th element]
# so the first three and last three characters are discarded

# stnew = stnew[-1] + stnew[:-1]
# stnew[-1]: This accesses the last character of stnew. (a word in which first letter was made last while encoding)
# stnew[:-1] : This accesses all characters of stnew except the last one.
# The last character is moved to the front, and the rest of the string is appended after it.

# word = "abcdefg12345xyz"

# Step 1: Remove 3 characters from the start and end
# stnew = word[3:-3]  # "defg12345"

#  Step 2: Move the last character to the front
# stnew = stnew[-1] + stnew[:-1]  # "5defg1234"
