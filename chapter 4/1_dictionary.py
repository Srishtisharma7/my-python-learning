# Dictionary is a collection of keys-value pairs.
#Syntax:
a = {
"1" : "srishti",
"key": "value",
"harry": "code",
"marks": "100",
"list": [1, 2, 9]             
}  # {"1" : "srishti"} as a key value pair is allowed too


print(a["key"]) # Output: "value"
print(a["list"]) # Output: [1, 2, 9] corresponding value to the list key

marks = {
"Harry": 100,
"Shubham": 56,
"Rohan": 23}
print (marks, type (marks))
#output: {'Harry': 100, 'Shubham': 56, 'Rohan': 23} <class 'dict'>
#or 
print (marks.items())
#Return a set-like object providing a view on the dict's items.
#outpit: dict_items([('Harry', 100), ('Shubham', 56), ('Rohan', 23)])

#print(marks [0]) ; error as no key named 0
print (marks ["Harry"])  
#will return harry marks or its corresponding value pair as harry key is defined

#marks = [["Harry", 100],] 
"""we can make list inside list to store value pair but cant find in one go unlike dictionary , computationally expensive"""

# PROPERTIES OF PYTHON DICTIONARIES
# 1. It is unordered.
# 2. It is mutable. (can change value pairs to the corresponding keys)
# 3. It is indexed.
# 4. Cannot contain duplicate keys.