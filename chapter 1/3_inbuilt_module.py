#4. Write a python program to print the contents of a directory using the os module.
#Search online for the function which does that.

import os  ##built in module

# Specify the directory path; use '.' for the current directory
directory_path = '/c'

try:
    # Get the list of all entries in the directory
    entries = os.listdir(directory_path)
    
    print(f"Contents of '{directory_path}':")
    for entry in entries:
        print(entry)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
except Exception as e:
    print(f"An error occurred: {e}")


"""Explanation:

Import the os module: This module provides a way of using operating system-dependent functionality like reading or writing to the file system.
Specify the directory path: Set directory_path to the path of the directory whose contents you want to list. Using '.' refers to the current working directory.
Retrieve directory contents: The os.listdir(directory_path) function returns a list of all entries (files and directories) in the specified directory. 

Handle exceptions: The try-except block manages potential errors:
FileNotFoundError: Raised if the specified directory does not exist.
PermissionError: Raised if there are insufficient permissions to access the directory.
Exception: Catches any other exceptions that may occur.
This program will print the names of all files and subdirectories in the specified directory. If you want to list only files or only directories, you can use os.path.isfile() and os.path.isdir() respectively to filter the entries.

For more advanced directory traversal, especially when dealing with subdirectories, consider using os.walk(), which allows you to iterate over all directories and files within a given directory tree. """

#following code can also be used

"""import os

# Select the directory whose content you want to list
directory_path = '/your/directory/path'

# Use the os module to list the directory content
contents = os.listdir(directory_path)

#print contents of the directory
print (contents)"""


# The os module in Python is a built-in library that provides functions for interacting with the operating system. 
# It allows you to perform a wide variety of tasks, such as reading and writing files, interacting with the file system, and running system commands.

import os

# if(not os.path.exists("dataos")):             # creates file when there is no other file of sae name, once rerun condition will show flase as file now has been created
#     os.mkdir("dataos")                   # creates a directory data os which has day 1 to 100 files built automatically

# for i in range(0, 100):
#     os.mkdir (f"dataos/Day{i+1}")

# if we have to rename the day (file name) to tutorials 1 to 100
# for i in range(0, 100):
#     os.rename (f"dataos/Day{i+1}", f"dataos/Tutorial i+1|")

import os
folders = os.listdir ("dataos")
print (folders)
for folder in folders:
    print (folder)    # lists out all the folders day 1 to day 100
    print(os.listdir(f"dataos/{folder}"))             # tells all the files of that folder as well if empty it shows[], or else it shows the file name

# make a file inside tutorial 7 named srishti  , file name will get printed there
# Day7
# ['srishti.py']
# Day9
# []
# Day8
# []


print(os.getcwd () )              #returns our current working directory
# os. chdir("/Users")              can change our directory




'''os. remove() removes a file.
os. rmdir(), removes an empty directory.
shutil.rmtree() deletes a directory and all its contents.'''






# Open the file in read-only mode
f = os.open("myfile.txt", os.O_RDONLY)

# Read the contents of the file
contents = os.read(f, 1024)

# Close the file
os.close(f)


# write only mode 

import os

# Open the file in write-only mode
f = os.open("myfile.txt", os.O_WRONLY)

# Write to the file
os.write(f, b"Hello, world!")

# Close the file
os.close(f)


# Create a new directory
os.mkdir("newdir")


# Run the "ls" command and print the output
output = os.system("ls")
print(output)  # Output: ['myfile.txt', 'otherfile.txt']


# Run the "ls" command and get the output as a file-like object
f = os.popen("ls")

# Read the contents of the output
output = f.read()
print(output)  # Output: ['myfile.txt', 'otherfile.txt']

# Close the file-like object
f.close()




# print(dir(os))
# It gives us a list of all the functions the OS module is composed of.


# os.getcwd( ):
# Here cwd is a short form for the current working directory. The function returns us the path of the directory we are currently in. It is important to know about our directory because when we are trying to import a file in python, the compiler searches for it in our current directory.
 
 
# os.chdir( ):
# It is used in case we want to change our directory. The new path is sent inside the parenthesis. If we want to access some files or folders from some other directory, we can use it.
 

# os.listdir( ):
# If we want to output the names of all the directories at a certain location, we can use this function.
 

# os.mkdir( ):
# To create a new directory or folder. The name is sent as a parameter inside the parenthesis.
 
 
# os.makedirs( ):
# To make more than on directory simultaneously.


# os.rename( ):
# To rename an already existing directory, we use this. We send the current name and new name of our directory as parameters.


# os.rmdir( ): 
# It deletes an empty directory.
 

# os.removedirs( ):
# We can remove all directories within a directory by using removedirs(). 
 

# os.environ.get( ):
# It will return us the environment variable. The environment variable must be set, or the function will return null.


# os.path.join( ): 
# It joins one or more path components. We can join the paths by simply using a + sign, but the benefit of using this function is that we do not have to worry about extra slashes between the components. So less accuracy still provides us with the same result.


# os.path.exists( ): 
# It returns us a Boolean value, i.e., either true or false. It is used to check whether a path exists or not. If it does, then the output will be true, otherwise false.


# os.path.isfile( ): 
# It returns true if the path is an existing regular file.


# os.path.isdir( ): 
# It returns true if the path is an existing directory.
