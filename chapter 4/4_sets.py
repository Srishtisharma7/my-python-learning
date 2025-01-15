#Set is a collection of non-repetitive elements.
s = {1,5,4,6}
#set and dictionaries are made using curly brackets
#but for empty set , use ()brackets not {} as {} are for empty dictionaries
e = set()
d = {}
print (type(e))               #<class 'set'>
print(type(d))                # <class 'dict'> 
                               
set = {1,5,32,54,5,5,5}
#5 repeating but in output its shown once only
print(set)        #{32, 1, 5, 54}

#here order is not maintained , hence properties are
# 1. Sets are unordered => Element’s order doesn’t matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. There is no way to change items in sets. [IMMUTABLE] but we can add and remove items from sets
# 4. Sets cannot contain duplicate values.


set2 = {2, 4, 2, 6}
print(set2)

info = {"Carla", 19, False, 5.9, 19}
print(info)

for value in info:
  print(value)

# Carla
# False
# 19
# 5.9