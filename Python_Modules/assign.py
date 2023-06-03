# It's the end of the semester and you got your marks from, Geometry, Algebra, Physics classes. 
# If the average score is 7 and above print "Good job!", 
# if the average score is between 6 and 4 print "You need to work harder!", 
# if the average score is below 4 print "Failed, you really need to work harder!".


#solution 
# Method 1 requiring the user to input the scores 

geometry_score = float(input("Enter your Geometry score: "))
algebra_score = float(input("Enter your Algebra score: "))
physics_score = float(input("Enter your Physics score: "))

average_score = (geometry_score + algebra_score + physics_score) / 3

if average_score >= 7:
    print("Good job!")
elif average_score >= 4:
    print("You need to work harder!")
else:
    print("Failed, you really need to work harder!")


# Method 2

# Define the marks for Geometry, Algebra, and Physics
geometry_mark = 8
algebra_mark = 6
physics_mark = 5

# Calculate the average score
average_score = (geometry_mark + algebra_mark + physics_mark) / 3

# Check the average score and print the corresponding message
if average_score >= 7:
    print("Good job!")
elif 4 <= average_score < 7:
    print("You need to work harder!")
else:
    print("Failed, you really need to work harder!")
