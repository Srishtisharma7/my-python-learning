# 6. Write a program to mine a log file and find out whether it contains ‘python’.

with open("/Users/srishtisharma/python/code harry/chapter 8/log.html") as f:
    content = f.read()

if("python" in content):
    print("Yes python is present")
else:
    print("No Python is not present")



# 7. Write a program to find out the line number where python is present from ques 6.

with open("/Users/srishtisharma/python/code harry/chapter 8/log.html") as f:
    lines = f.readlines()
#read lines
line_no = 1
for line in lines:
    if("python" in line):
        print(f"Yes python is present. Line no: {line_no}")
        break
    line_no += 1    # line no. gets incresed every time and it search in the next line
#for loop iterates and search in every line, if found print the statement and line no. then breaks and stops execution
# if not found then executes the else statement
else:
    print("No Python is not present")