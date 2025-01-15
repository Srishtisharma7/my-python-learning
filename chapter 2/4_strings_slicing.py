#strings are immutable eg: "harry" cant be "henry" to change , we have to make another string ; although strings can be sliced [existing strings cant be changed

""" name = "harry"
h is at 0th index  , 1 is at 1st and y is 4th index.{count starts from 0}
if we count from back y is -1 , r is -2 , h is -5 index {count starts from -1 from back}
to count string length = len(name) ; """

#to slice string syntax is
name = "harry"
nameshort = name[0:3]    # start from index 0 all the way till 3 (excluding 3) 0, 1, 2 index total 3 sliced 
#[ brackets] to define or declare the index positions of string
print (nameshort)

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

apple = "my fav fruit is apple"

print("Lets use a for loop\n")
for character in apple:
    print(character)            # prints all characters of apple

character1 = name[1]
print (character1)
#return character at index 1 of name defined by [1}

                                        #negative slicing
                                         
print (name[-4: -1])            #convert negative indexing into positive indexes 
print (name [1:4])                #result stays same             


print (name [ :4])                 #means started from 0 only, excluding index 4   [0:4]                 #haar
print (name [:5] )                # includes all elements from 0 to including index 4   [0:5]            #harry
print (name [1:])             # till the last index n-1, is same as print (name [1:5])                   #arry
print (name [1:5])                    #here last element is included                                     #arry
print(name[:])                   #includes all elements                                                  #harry


"""SLICING WITH SKIP VALUE
We can provide a skip value as a part of our slice like this:"""
#example 1

word = "amazing"                     #"0123456" = amazing 7 elements

print (word[1: 6: 2]  )     

#[1:6 ] gives 12345 tak excluding 6th index element ie; mazin
#now after every 2nd skip , element is printed  ie; 1st = m , 3rd = z , 5th = n
  # "mzn" is output

"""example 2""" 

new = "0123456789"
print (new[1:7:3])
# 123456 tak excludes 7 , then skip three three so output comes = 14

b = "abcdefghijklmnopqrstuvwxyz"
print(b[1:9:4])
# ecludes a and j(9th), bcdefghi then print every 4th element ; output = bf