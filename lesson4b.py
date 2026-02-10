# loops-> sometimes we maty need to do a piece of work a number of  repeated times in such cases we may use loops. 
# A loop is a control structure that allows us to execute a block of code repeatedly until a certain condition is met
#There are two loop in python i.e. : The for loop and the while loop.

# Below is the syntax of a loop in python:
"""
for variable in a range(n):
    #block of code to be executed
"""
for greeting in range(5):
    print("hello moses" , greeting)

print("---------------------")

for number in range(10 , 21):
    print(number)


print("___________________")
# find the even number in the range of 50 to 71
for number in range(50 , 71 , 2):
    print(number)


print("___________________")
# create a python that prints the odd numbers from 100 to 150
for number in range(101 , 151 , 2):
    print(number)
for number in range (100,151):
    if number % 2 !=0:
        print(number)

print("___________________")
# create a program that prints the multiples of three from 201 to 150
for number in range (201 , 149 , -1):
    if number %3 ==0:
        print(number)

print("___________________")
#create a python program that prints the leap years ni btn 2000 and 2024
for number in range (2000, 2025):
    if number %4==0:
        print(number)
