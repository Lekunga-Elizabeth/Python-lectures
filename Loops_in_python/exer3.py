# Write a program that takes a list of numbers and returns the sum of all the even numbers in the list.
numbers = [3, 9, 2, 7, 5, 10, 6, 4]

# Initialize a variable to store the sum of even numbers
even_sum = 0

# Iterate over each number in the list
for num in numbers:
    # Check if the number is even
    if num % 2 == 0:
        # Add the even number to the sum
        even_sum += num

print("The sum of even numbers is:", even_sum)


# Write a program in python that takes a list of numbers and returns the maximum number in the list

numbers = [3, 9, 2, 7, 5]

# Sort the list in ascending order
numbers.sort()

# Get the last element, which is the maximum number
maximum = numbers[-1]

print("The maximum number is:", maximum)




        


