# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the different files. 
# Place these files in a folder for a 13 – year old.


def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"                # function defined to create tables
    
    with open(f"/Users/srishtisharma/python/code harry/chapter 8/tables/table_{n}.txt", "w") as f:
        f.write(table)                        

#here, for loop iterates and generate table, and table is written inside files [in "table" folder] named according to 'n'value
#ie; no whose table we writing 

for i in range(2, 21):        #table 2 to 20
    generateTable(i)              #call function


''' A for loop iterates through the range 2 to 20 (inclusive).
Calls the generateTable(i) function for each number i, generating and saving the corresponding multiplication table'''





# f = open('myfile.txt', 'r')
# i = 0
# while True:
#   i = i + 1
#   line = f.readline()
#   if not line:
#     break
#   m1 = int(line.split(",")[0])
#   m2 = int(line.split(",")[1])
#   m3 = int(line.split(",")[2])
#   print(f"Marks of student {i} in Maths is: {m1*2}")
#   print(f"Marks of student {i} in English is: {m2*2}")
#   print(f"Marks of student {i} in SST is: {m3*2}")

#   print(line)
