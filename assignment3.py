#Below is a program that calculates the monthly an employee should make to the national health insurance fund as per grossincom
gross_salary = float(input("Enter your salary here"))
if gross_salary > 0 and gross_salary <=5999:
    print("Your monthly contribution is ksh 150.00")
elif gross_salary >5999 and gross_salary <=7999:
    print("Your monthly contribution is ksh 300.00")
elif gross_salary >7999 and gross_salary <=11999:
    print("Your monthly contribution is ksh 400.00")
elif gross_salary> 11999 and gross_salary <= 14999:
    print("Your monthly contribution is ksh 500.00")
elif gross_salary > 14999 and gross_salary <=19999:
    print("Yor monthly contribution is 600.00")
elif gross_salary > 19999 and gross_salary <= 24999:
    print("Your monthly contribution 750.00")
elif gross_salary > 24999 and gross_salary <= 29999:
    print("Your monthly contribution is 850.00")
elif gross_salary > 29999 and gross_salary <= 49999 :
    print("Your monthly contribution is 10000.00")
elif gross_salary > 49999 and gross_salary <= 99999:
    print("Your monthly contribution is 1500.00")
else:
    print ("Your monthly contribution is ksh 2000.00")
