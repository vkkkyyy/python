#create a python program that is able to determine whether a number entered is an odd number or an even number.
number = int(input("Enter number :"))

if number % 2 == 0:
    print("number is an even number")
else :
    print ("the number is odd")
#create a python program that is able to determine whether a person can donate blood on the age and weight of a person. if the weight is greater than 50 kg and is 18 yrs and above,  then the person can donate ,else not possible.
age = int(input("enter age:"))
weight = int(input("Enter weight: "))

if age >= 18 and weight > 50:
    print("can donate")
else : 
    print("Not possible")