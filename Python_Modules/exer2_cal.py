"""
Exercise 3
You want to buy something from Amazon. The seller charges different prices for shipping cost
based on location. For US it's 5$ for Europe it's 7$ for Canada it's 3$ for other places it's 9$
Create a program that:
● Reads the cost of the product
● Reads your location
● Print the amount of money you have to pay
Ouput: "You have to pay 23$, 20$ for the product and 3$ for shipping cost
"""

# funtions are define within a class an you invoke them on instances and can be call from anywhere  a method are invoke on a variable 
# Solution
product_cost=float(input("Enter the product cost : "))
location=str(input("Enter your location (USA,Europe, Canada, other): "))
if location.upper()=="USA":
    Shipping_cost=5
elif location.upper()=="EUROPE":
    Shipping_cost=7
elif location.upper()=="CANADA":
    Shipping_cost=3
else:
    Shipping_cost=9
Total_cost=Shipping_cost + product_cost
print(Total_cost)

#Method 2 using a module 