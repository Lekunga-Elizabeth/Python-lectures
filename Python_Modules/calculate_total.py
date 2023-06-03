from calculate_total_cost import calculate_total
product_cost=float(input("Enter the product cost : "))
location=input("Enter your location (USA,Europe, Canada, other): ")
Total_cost=calculate_total(product_cost, location)
print("You have to pay   $", Total_cost)