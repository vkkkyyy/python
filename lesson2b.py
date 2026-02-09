#tulpe
# A tuple is an immutable type of a list (it cannot change)
#to introduce a tuple , we use the parenthesis()

counties= ("Nairobi", "Mombasa", "Nakuru", "Eldoret", "Kajiado", "Kisii")
print(counties)
print(type(counties))

#slicing of tuples
print(counties[3:])

#accessing items of a tuple by use of index
print(counties[5])

#note :below will generate an error
#ATTRIBUE ERROR
counties.append("Machakos")
print(counties)
