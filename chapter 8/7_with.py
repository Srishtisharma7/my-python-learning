f = open("file.txt")
print(f.read())
f.close()

# The same can be written using with statement like this:
with open("file.txt") as f:
    print(f.read())    # Read and print the contents of the file

# You dont have to explicitly close the file
#out of with statement, file closes, write all program before it only