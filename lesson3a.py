#Boolean- this is a data type that evaluates either true or false 

isRaining = False
print(isRaining)
print(type(isRaining))

paidloan = True
print(paidloan)
print(type(paidloan))

#comparison operators : they are sued to compare two or more statement and they usually return a boolean answer

number1 = 2
number2 = 5

print("Is number1 greater than number2?" , number1 > number2)
print("Is number1 less than number2?" , number1 < number2)
print("Is number1 greater than or equal to number2?" , number1 >= number2)
print("Is number1 less than or equal to number2?" , number1 <= number2)
print("Is number1 equal to number2?" , number1 == number2)
print("Is number1  not equal to number2?" , number1 != number2)


#logical operators
#logical AND
#it returns true if an only if the condition / statement evaluates to be true
print((3 > 1) and (7 > 6))


#logical or
#It evaluates to true if one of the statement/condition is true
print((3 > 1) or (7<6))

#Logical not to negate a statement/ condition
#It is usd to negate a statement/condition
print(not(90>70))