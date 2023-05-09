# Propose a program to calculate Simple Interest

# Simple Interest = (P x T x R)/100 Where, P is the principal amount T is the time and R is the rate

# Take P, T and R as user inputs.

# solution
#1. firstly identification of your inputs  which in this case we have. principal(p), Time(T) and Rate(R) these are what we will get from user.

principal = int(input("Enter the principal amount: "))

time = int(input("Enter the time in years: "))

rate = int(input("Enter the rate of interest: "))

# calculate the simple interest
simple_interest=(principal * time * rate)//100

# print the result
print('the simple_interest is', simple_interest)


