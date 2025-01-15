#Python lists are containers to store a set of values of any data type or multiple data types.

friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

#"str" = "harry" if we assign y at a[3] index its not possible as strings are immutable
#a[3] = 'y'    "str" object does not support item assignment, no changes in existing string
#but in lists we can change one element of the entire thing defined .
# Unlike Strings lists are mutable, are flexible and can be changed and updated in between

print (friends [0])                    #apple
friends [0] = "Grapes"
print (friends [0])                    #index o changed to grapes
print (friends [6])                    #rohan


#list slicing and indexing is similar to strings
print(friends [1:4])             #value at 1 2 3 index, excluding 4th


if "Ha" in "Harry":      # in keyword
    print( "Yes")


'''list comprehensions'''
# List Comprehension is an elegant way to create lists based on existing lists.

myList = [1, 2, 9, 5, 3, 5]

# squaredList = []
# for item in myList:
#     squaredList.append(item*item)

squaredList = [i*i for i in myList]

print(squaredList)    



# exapmle:
lst = [i*i for i in range (10)]
print(lst)

lst = [i*i for i in range(10) if i%2==0]
print(lst)

# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# [0, 4, 16, 36, 64]
