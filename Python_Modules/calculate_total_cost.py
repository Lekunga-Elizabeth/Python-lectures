def calculate_total(product_cost,location):
    product_cost=float(input("Enter the product cost : "))
    location=input("Enter your location (USA,Europe, Canada, other): ")
    if location.upper()=="USA":
        Shipping_cost=5
    elif location.upper()=="EUROPE":
        Shipping_cost=7
    elif location.upper()=="CANADA":
        Shipping_cost=3
    else:
        Shipping_cost=9
    Total_cost=Shipping_cost + product_cost
    return Total_cost
