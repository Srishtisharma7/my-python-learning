marks = {
"Harry": 100,
"Shubham": 56,
"Rohan": 23}

# a.items(): Returns a list of (key,value)tuples.
print (marks.items())
#Return a set-like object providing a view on the dict's items.


# • a.keys(): Returns a list containing dictionary's keys.
print (marks. keys ( )) 
#output:
print(marks. values ())
#ouput: 


# • a.update({"friends":}): Updates the dictionary with supplied key-value pairs.
marks. update({"Harry": 99})
marks.update({"Harry": 99, "Renuka": 100})
#update then the key which is not available gets added in the dictionary (mutable)
print (marks)


# • a.get("name"): Returns the value of the specified keys (and value is returned
print(marks.get("shivika"))
#no shivika key so "none" is the output
print(marks.get("Harry"))
# harry ke marks 99 [after updattion] returned here


print (marks.get ("Harry2")) # Prints None 
#print(marks ["Harry2"]) # Returns an error
