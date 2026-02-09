#A dictionary is a data type that stores data in terms of key- value pair.
# Its introduced by the use of curly braces{}
#The values stored inside of any dictionary can be of any data type.
#To access the values in a dictionary we use the keys


phonebook ={
    "Benson" :"25410326125"
    "May"  "25498764389"
    "Stephen"  "25495640875"
}

# showing the entire dictionary
print(phonebook)
print(type(phonebook))

#print out benson's number
print(phonebook["Benson"])

print('============================')

player ={
    "name" : "messi",
    "age": 40,
    "teams"  : ["PSG" , "Barcelona" , "Argentina"] ,
    "more" :{
        "children": 3 ,
        "phone" : (254739034689 , 25497487778728 ,254807566489)
    }
    
}
#print barcelona- the 2nd team he played for
print(player["teams"][1])

#print for messi second number
print(player["more"]["phone"][1])