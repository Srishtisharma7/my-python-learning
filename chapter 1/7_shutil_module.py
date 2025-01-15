'''Shutil is a Python module that provides a higher level interface for working with file and directories. The name "shutil" is short for shell utility. 
It provides a convenient and efficient way to automate tasks that are commonly performed on files and directories'''


import shutil

# The following are some of the most commonly used functions in the shutil module:

# shutil.copy(src, dst): This function copies the file located at src to a new location specified by dst. 
# If the destination location already exists, the original file will be overwritten.

# shutil.copy2(src, dst): This function is similar to shutil.copy, but it also preserves more metadata about the original file, such as the timestamp.

# shutil.copytree(src, dst): This function recursively copies the directory located at src to a new location specified by dst. 
# If the destination location already exists, the original directory will be merged with it.

# shutil.move(src, dst): This function moves the file located at src to a new location specified by dst. This function is equivalent to renaming a file in most cases.

# shutil.rmtree(path): This function recursively deletes the directory located at path, along with all of its contents. 
# This function is similar to using the rm -rf command in a shell.


# Copying a file
shutil.copy("src.txt", "dst.txt")

# Copying a directory
shutil.copytree("src_dir", "dst_dir")

# Moving a file
shutil.move("src.txt", "dst.txt")

# Deleting a directory
shutil.rmtree("dir")