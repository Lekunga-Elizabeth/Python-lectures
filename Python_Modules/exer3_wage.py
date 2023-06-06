"""
Python Scenario Exercises
Exercise 1
In a company the monthly salary of an employee is calculated by: the minimum wage 400$ per
month, plus 20$ multiplied by the number of years employed, plus 30$ for each child they have.
Create a program that:
● Reads the number of years employed
● Reads the number of children the employee has
● Prints the total amount of salary the employee makes
Output: "The total amount is 560$. 400$ minimum wage + 100$ for 5 years experience +
60$ for 2 kids"
"""

#Solution

years_employed = int(input("Enter the years employed: "))
num_of_children = int(input("Enter the number of children per employee: "))

minimum_wage_per_month = 400
salary_per_year = 20
salary_per_child = 30

if years_employed == 5:
    minimum_wage_per_month = minimum_wage_per_month + 100
elif years_employed < 5:
    minimum_wage_per_month = minimum_wage_per_month + (years_employed * 60)

total_salary = minimum_wage_per_month + (years_employed * salary_per_year) + (num_of_children * salary_per_child)

print(total_salary)