# Build a custom Python module called math_utils.py that provides basic math operations.
# Implement functions like add(a, b), subtract(a, b), multiply(a, b), and divide(a, b).
# In your main script, import the math_utils module and perform calculations using the defined math functions

#defination of functions 
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


# module operation in python / so no module exist in python as Math_utils so we need to creat a custome module by saving our file 
# in the file name Math_utils.py it will help import the custom module that we can use 

import math_utils

calculate_add = math_utils.add(10, 3)
print("Addition:", calculate_add)

calculate_subtract = math_utils.subtract(15, 4)
print("Subtraction:", calculate_subtract)

calculate_multiply = math_utils.multiply(12, 6)
print("Multiplication:", calculate_multiply)

calculate_divide = math_utils.divide(20, 2)
print("Division:", calculate_divide)
