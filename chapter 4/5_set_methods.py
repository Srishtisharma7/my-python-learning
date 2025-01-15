s = {1, 5, 32, 54,5, 5, 5, "Harry"}

print(s, type(s))       #class set

s.add(566)
print(s, type(s))
#{32, 1, 5, 'Harry', 54, 566}   <class 'set'>

s.remove(1)
print(s, type(s))
#{32, 5, 54, 566, 'Harry'}       <class 'set'>

len(s)
#Returns 5, the length of the set

s.pop()
#Removes an arbitrary element from the set and return the element
# Raises a KeyError if the set is empty.


# s.clear():empties the set s. This method clears all items in the set and prints an empty set.

# s.union(): Returns a new set with all items from both sets.
s1 = {1, 45, 6}
s2 = {7, 8, 1, 78}
print(s1.union(s2))

# s.intersection(): Return a set which contains only item in both sets
print(s1. intersection (s2))
#output:
# {1, 6, 7, 8, 45, 78}
# {1}

# s.difference - :
#Returns a new set with elements in the set but not in others.
print(s1.difference(s2))  # Output: {45, 6}

# s.symmetric_difference or ^
#Returns a new set with elements in either set but not both.
print(s1.symmetric_difference(s2)) 
 # Output: {6,7,8,45,78}
#  prints only items that are not similar to both the sets. The symmetric_difference method returns a new set whereas symmetric_difference_update method updates into the existing set from another set.


s3 = {1, 2}
print(s3.issubset(s1))  # Output: False

print(s1.issuperset(s3))  # Output: False

s4 = {6, 7}
print(s1.isdisjoint(s4))  # Output: False
#Returns True if the set has no elements in common with other.


# copy() : Returns a shallow copy of the set.
s_copy = s1.copy()
print(s_copy)  # Output: {1, 45, 6}


# update(): Updates the set with the union of itself and others.()
s1.update(s2)
print(s1)  # Output: {1, 6, 7, 8, 45, 78}


#intersection_update: Updates the set to keep only elements also found in others.()
s1.intersection_update({2, 3, 5})
print(s1)  
# Output: set()


# difference_update: Updates the set to remove elements found in others.()
s1.difference_update({3, 5})
print(s1)  
# Output: set()


#symmetric_difference_update: Updates the set to the symmetric difference with other.
s1.symmetric_difference_update({1, 4})
print(s1)  
# Output: {1, 4}


s.discard(5)  # No error even though 5 is not in the set
#Removes an element if it exists; does nothing if the element is not found.
