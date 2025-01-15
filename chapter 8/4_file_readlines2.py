# '''for lines individually , f.readlines() print or read the line now as string every time we write the function''' 

f = open("/Users/srishtisharma/python/code harry/chapter 8/file.txt")
#we again open the file

# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))             
# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4, type(line4))

# line5 = f.readline()
# print(line5 =="")          #no 5th line , so we check if its equal to balnk space , so yes here it returns true

#we can use this using loop as well

line = f.readline()       
while(line != ""):     # or if not line : break  #jab tak line empty na ho , tab tak print line
    print(line)
    line = f.readline()

f.close()


# output for both :  
# Harry is a good boy
#  <class 'str'>
# I am a second line
#  <class 'str'>
# This is amazing
#  <class 'str'>
# Twinkle Twinkle little star <class 'str'>
# True


# Harry is a good boy

# I am a second line

# This is amazing

# Twinkle Twinkle little star