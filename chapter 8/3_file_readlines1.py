f = open("/Users/srishtisharma/python/code harry/chapter 8/file.txt")

lines = f. readlines ()
print(lines, type(lines))
f. close()

# #readline returns lines of a file in a list
# # output: ['Harry is a good boy\n', 'I am a second line\n', 'This is amazing\n', 'Twinkle Twinkle little star'] <class 'list'>



#the writelines() method in Python writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple.
#writelines() method does not add newline characters between the strings in the sequence. 
# If you want to add newlines between the strings, you can use a loop to write each string separately:

f = open('myfile.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()

