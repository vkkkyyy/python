# 1. Input: Gross Salary
gross_salary = float(input("Enter gross salary: "))

# 2. Determine monthly contributions using if-else
if gross_salary <= 30000:
    contribution_rate = 0.05  # 5%
elif gross_salary <= 60000:
    contribution_rate = 0.10  # 10%
else:
    contribution_rate = 0.15  # 15%

monthly_contribution = gross_salary * contribution_rate

print(f"Monthly Contribution: {monthly_contribution:.2f}")

# 3. Sum of contributions over a period (e.g., 12 months)
total_contribution = 0
months = 12

for month in range(1, months + 1):
    total_contribution += monthly_contribution
    print(f"Month {month}: Contribution = {monthly_contribution:.2f}")

print(f"Total Contribution after {months} months: {total_contribution:.2f}")
