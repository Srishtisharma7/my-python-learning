'''
a = "a very long string with emails"

emails = []               # generated data {e mails} to store them into file
3 seconds it took


The random-access memory is volatile, and all its contents are lost once a program terminates in order to persist the data forever, we use files.
RAM is fast, so we use it while executing the program, while SSD are to store extracted data.
A python program can talk to the file by reading content from it and writing content to it. '''

# There are 2 types of files:
# 1. Text files (.txt, .c, etc)
# 2. Binary files (.jpg, .dat, etc)
# Python has a lot of functions for reading, updating, and deleting files.


# make a file.text first , if name dont work copy the path
#open is a built in function , by default it opens in 'r' mode, f.read reads contents and pass it to data variable
#always close the file once work is done

f = open ("/Users/srishtisharma/python/code harry/chapter 8/file.txt", "r") # takes two arguments, one file path or name , another opening mode
text = f.read()
print(text)



