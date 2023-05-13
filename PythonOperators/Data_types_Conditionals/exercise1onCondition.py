# conditional statement 

#. exercise 1. on conditional 
#Propose a script that checks if a number is divisible by 2.
#If the number is divisible by 2 it should print “hey this number is divisible by 2”  otherwise it should print “hey this number is not divisible by 2”

#solution( in this exercise we used the modulous operation which is '%' and the equality operaiton '==')

a=60
if (a % 2 == 0):
    print("Hey, this number is divisble by 2")
else:
    print("Hey,number is not divisible by 2")
    
# exercise 2.

# Write an if statement that asks for the user's name via input() function. 
# If the name is “Acha” make it print "Welcome on board Acha” Otherwise make it print "Good morning Engr. Akum

#Solution
#Get Name from user
name=str(input("what is your name:"))
if name=="Acha":
    print("Welcome on board Acha")
else:
    print("Good morning Engr ", name)
    