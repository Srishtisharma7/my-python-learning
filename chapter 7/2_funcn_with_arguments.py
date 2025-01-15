#Function with arguments

def goodDay (name) :                   #one argument passed
   print ("Good Day, " + name)         #string added or catenation

goodDay ("Harry")   #this will be passed as argument in name variable and  
goodDay("Rohan" )   #every time we call it withh diff names, it gets printed
goodDay ("Divya")


#two arguments passed

def goodDay(name, ending):             
    print("Good Day, " + name)            # one name added with goodday
    print(ending)                        #another printed in next line
    return "ok"

goodDay("Harry", "Thank you")  
           #function called with arguments given
goodDay ("Rohan","Thank you")
goodDay ("Divya", "Thanks")


