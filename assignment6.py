# 1.A function that takes no parameters , usus arithmetic operators to calculate the area of a rectangle and prints the results
def area ():
    length= 20
    width= 15
    area = length * width
    print (area)

area()
print("-----------------------")

# 2. Afunction that accepts two perimeters , returns their sum , difference , products and division
def arithmetic_operations(num1, num2):
    sum = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    division = num1 / num2
    return sum , difference, product , division
result= arithmetic_operations(10,5)
print("The sum is :", result[0])
print("The difference is:", result[1])
print("The product is:", result[2])
print("The division is", result[3])

print("===========================")
 # 3. A function that accepts a number (uses input functions) , checks whether the number is positive , negative or zero and prints the result , using if , else, elif
def check_number():
    num= int(input("Enter a number: "))
    if num > 0:
        print("The number is positive")
    elif num < 0:
        print("The number is negative")
    else :
        print("The number is zero")
    check_number()


print("========================")


# 4. A function that accepts the number n , uses a loop and calculates the sum of numbers from 1 to n 
def sum_of_num(n):
    sum =0 
    for i in range(1,n+1):
        sum +i
    print("The sum of numbers from 1 to",n, "is :", sum)
n=int(input("Enter a number :"))
sum_of_num(n)

print("========================")

#5. A function that accepts a number , uses a while loop and calculates the square of numbers from 1 to that number 
def square_of_numbers(n):
    i=1
    while i<=n:
        square= i**2
        print("The square of", i , "is :", square)
        i+=1 
n= int(input("Enter a number: "))
square_of_numbers(n)



