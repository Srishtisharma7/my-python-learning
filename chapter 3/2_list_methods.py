friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(friends)
friends.append("Harry")           # adds "harry" at the end of the list
print(friends)
# output :['Apple', 'Orange', 5, 345.06, False, 'Aakash', 'Rohan', 'Harry']


l1 = [1, 34,62, 2, 6, 11]
#sort in ascending
l1.sort()
print (l1)          # ascending output :[1, 2, 6, 11, 34, 62]

l1.reverse()
print (l1)          # output:[62, 34, 11, 6, 2, 1]

l1.insert(2, 333333)  #(index:value) 
# so after index 2 333333 is added and hence we are able to
# Insert 333333 in a way that its index in the list is 3
print (l1)                        # output : [62, 34, 333333, 11, 6, 2, 1]
                               
l1.insert(4 ,"srishti")             #this will add "srishti" at 4 index
print(l1)                       #after 4 index element is added
# output : [62, 34, 333333, 11, 'srishti', 6, 2, 1]
        
l1.pop (3)                              #Will delete element at index 3 and return its value.
print (l1)                                       # output:[62, 34, 333333, 'srishti', 6, 2, 1] (removed 11 after 3rd index)

value = l1.pop(3)     # or print(l1.pop(3))
print(value)           #return the value which is popped out ; here 11
#after updated list ; srishti is popped out as it is at the index now after 3 to be pooped out
print(l1)
# output:[62, 34, 333333, 6, 2, 1]

l1.remove(2)
#Will remove 2 from the list.
print(l1)
#output final:[62, 34, 333333, 6, 1]

'''example 2'''

l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
print(l.index(1))    # 2
print(l.count(1))   # 3
m = l.copy()
print(l)    # [11, 45, 1, 2, 4, 6, 1, 1]

l.insert(1, 899)  # insert 899 at index 1 11, [899, 45, 1, 2, 4, 6, 1, 1, 900, 1000, 1100]

m = [900, 1000, 1100]
l.extend(m) # open m and add it to l
print(l) # [11, 899, 45, 1, 2, 4, 6, 1, 1, 900, 1000, 1100, 900, 1000, 1100

k = l + m
print(k)
