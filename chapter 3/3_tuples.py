# A tuple is an immutable data type in python.

a = (1)
print (type (a))     #int 

a = (1, )
print(type(a))       #tuple with one element

a = (1, 2, 5, 6)
print(type(a))       #tuple

a = ()
print(type(a))         #empty tuple

a = (1,45, 342, 3424, False, "Rohan", "Shivam")
print(type(a))                      #tuple ; its fixed cant be changed or updated
print(a[-1])         # for -ve indexing , length -1 = here,7-1 =6 so -1 is actually 6th index "shivam"

#a [0] = 453       #tuple' object does not support item assignment; its immutable unlike lists


tup = (1, 2, 76, 342, 32, "green", True)
if  342 in tup:
  print("Yes 342 is present in this tuple")

tup2 = tup[1:4]  # tuple sliced
print(tup2)


"""tuple methods"""

a.count (1)
#a count (1) will return number of times 1 occurs in a tuple
a.index (1) 
#will return the index of first occurrence of 1 in a tuple

a = (1,45,342,3424,False, 45, "Rohan", "Shivam")
print(a)              

no = a.count(45)
print(no)                       # output: 2 as 45 appear twice

i = a.index(45)
print(i)                          # output: 1 ; count index of first occurence only

i = a.index(3424)
print(i)                          # output: 3

print(len(a))                # 8 length


# Concatenation: Tuples can be concatenated using the + operator.
tuple1 = (1, 2, 3) 
tuple2 = (4, 5, 6)
concatenated = tuple1 + tuple2
print (concatenated) 
# Output: (1, 2, 3, 4, 5, 6)


# 2. Repetition: Tuples can be repeated using the * operator.
my_tuple = (1, 2, 3)
repeated = my_tuple * 3
print(repeated)
# a Output I (1, 2, 3, 1, 2, 3, 1, 2, 3)


# 3. Membership: You can check if an item exists in a tuple using the 'in" keyword.
my_tuple = (1, 2,3)
print(2 in my_tuple)
print(4 in my_tuple)
# # Output: True
# # Output: False


# 4.Min and Max: Use the min() and max() functions to get the smallest and largest elements in a tuple.
my_tuple = (3, 1,4, 2)
print(min(my_tuple))
print(max(my_tuple))
# # Output: 1
# # Output: 4


# 5. Slicing: Tuples support slicing to create a new tuple from a subset of the original.
my_tuple = (1, 2, 3, 4, 5)
sliced = my_tuple[1:4]
print(sliced) 
# Output: (2, 3, 4)


# 6. Unpacking: Tuples can be unpacked into individual variables.
my_tuple = (1, 2, 3)
a, b,c = my_tuple
print(a, b, c) 
# Output: 1 2 3


#Manipulating Tuples
# Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.
# Example:

countries = ("Spain","England","Germany" ,"Italy", "India",)
temp = list(countries)         # make it list , store in temp
temp.append( "Russia" )             # add item
temp.pop (3)                        #remove item 
temp[2]= "Finland"                  # change item 
countries = tuple(temp)               # after changes , tuple it back from temp
print(countries)

# output" ('Spain', 'England', 'Finland', 'India', 'Russia')