# Write a Python function called calculate_factorial that takes a positive integer as input and calculates its factorial using a loop. 

# The factorial of a number n is the product of all positive integers from 1 to n.

def calculate_factorial(n):
    if n ==0:
        return 1
    else:
        return n * calculate_factorial(n-1)
print(calculate_factorial(0))