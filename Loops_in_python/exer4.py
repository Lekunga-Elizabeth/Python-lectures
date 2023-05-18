# Write a Python program that uses a while loop to repeatedly prompt the user to enter positive numbers, and stops when the user enters -1

sum=0
while True:
    num = int(input("Enter a positive number or enter -1 to exit : "))
    if num == -1:
        break
    
    if num > 0:
        sum=sum+num
        
    else:
        print("invald input enter a positive number")
print("the sum of the positive number is : ", sum)
        