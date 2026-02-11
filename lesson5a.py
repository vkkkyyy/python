#Python functions
# they are a block ofcode/ statements that performs a given task/action. They ca be re-used through out the programm to perform different tasks .
#Functions are defined using the 'def' key word
# we have two main types of functions i.e. 
#1. In built functions-> they come pre installed with the interpreter i.e. print() , pop() , range() , append() etc...
# 2. They are created by a programmer to solve a given task that suits the entire program.
# To define a function you need to give it a name followed by parenthesis.
# For the functions , it is usually indented and to involve a function we use the function names.


def greetings():
    print("Hello , how are you?")


#below we call the function by use of its name
greetings()
print("===================")


#addition function
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The sum of the number is :", sum)
addition()
print("=================")


## create a function that  is able to multiply three values
def multiplication():
    num3 =30
    num4 = 55
    num5 = 12
    times = num3 * num4 * num5
    print("The multiplication of the numbers is:", times)
multiplication()
print("=================")

# belowis a division function
def divide ():
    number1 = int (input("enter the first number"))
    number2 = int (input("enter the second number"))
    quotient = number1 / number2
    print("The answer is:", quotient)
divide()
print("-------------")

for function in range(3):
    divide()
divide()

