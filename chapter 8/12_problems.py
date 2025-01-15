# 8. Write a program to make a copy of a text file “this. txt”

with open("/Users/srishtisharma/python/code harry/chapter 8/this.txt") as f:
    content = f.read()

with open("/Users/srishtisharma/python/code harry/chapter 8/this_copy.txt", "w") as f:
    f.write(content)

# open this.txt in read mode, then content is write or copied into this_copy.txt file while autoamtically opening it in w mode and saving it as well




# 9. Write a program to find out whether a file is identical & matches the content of another file.

with open("/Users/srishtisharma/python/code harry/chapter 8/this.txt") as f:      # open both files in read mode
    content1 = f.read()

with open("/Users/srishtisharma/python/code harry/chapter 8/this_copy.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes these files are identical")

else: 
    print("No these files are not identical")


#program can be used to check the content of any two files , just change the path    




# 10. Write a program to wipe out the content of a file using python.

with open("this_copy.txt", "w") as f:
    f.write("")
#write blank will wipe out all the other content of the file and print blank empty space


# 11. Write a python program to rename a file to “renamed_by_ python.txt.

with open("old.txt") as f:            #put the directory right of the file u want to rename
    content = f.read()

with open("renamed_by_python.txt", "w") as f:    
    f.write(content)

#the most convinient way to rename a file is to shift its content into a new file and deleting the old file