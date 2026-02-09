#Python lists
#Alist in python is a collection of items that ordered in a certain way.
#A list is introduced by the use of squre brackets[]
#The items of a list are stored inside of inside of indexes. Note :In programming we start counting from index zero(0).bmw , benze , hiance ,....
#A list is mutable i.e the contents of a list can be changed.

cars = ["BMW" , "Benze" ,"Audi", "Prado", "McLarel" "Ferrari", "lamborghini"]

print(cars)
print(type(cars))

#Accessing items of a list
print(cars[2])
print("the car on index 4 is:", cars[4])

#list slicing- this is creating a list from a bigger list
print(cars[4:])

#printing from index 0 to index 3
print(cars[:4])

#printing grom audi to ferrari
print(cars[2:5])

#list- mutability
#we use the function append to add an item at the end of a list
cars.append("Ferrari")
print(cars)

cars.append("Prado")

#we use the pop fuction to remove an item at the end of the list
cars.pop()
print(cars)

#we can use an index to add items to a list
cars[5] = "Pajero"
print(cars)

#we can use the sort function to sort out items in alphabetical order
cars.sort()
print(cars)

# we can use the sort function to sort out items in alphabetical order
cars.sort(reverse=True)
print(cars)
del cars[4]
print(cars)
cars.pop(4)
print(cars)

cars.remove("BMW")
print(cars)