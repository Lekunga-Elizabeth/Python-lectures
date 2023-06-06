"""
An internet cafe has 2 ways of charging. If the user is a member pays 2$/hour, Else the user
pays 5$. Find if someone is a member or not and calculate the price based on how many hours
the user spend. If the user is a member the tax is 10% else the tax is 20%.
Create a program that:
● Reads how many hours the user spend
● Check if is a member
● Add the proper tax fee
● Print the total amount the user has to pay
"""

# solution
member=input("Enter yes if you are a member and Enter no if you are not a member :")
number_of_hours_spend=int(input("Enter number of hours spend on the internet :"))

price_per_hour_for_members=2
price_per_hour_for_non_members=5
tax_fees_for_members =10
tax_fees_for_non_members=20

if member=="yes":
    total_cost=(price_per_hour_for_members*number_of_hours_spend)+tax_fees_for_members
else:
    if member=="no":
        total_cost=(price_per_hour_for_non_members*number_of_hours_spend)+tax_fees_for_non_members
        
print=f"The total cost is {total_cost}$."
