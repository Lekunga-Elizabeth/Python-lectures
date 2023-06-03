# Create two variables x and y, and initially set them each to a different number. Write a python script that swaps both values.

# all this methods below are the same solution to all
#Example: x = 10, y = 20
#Output: x = 20, y = 10

#solution without defining the function 
#initials  befor swapping 
x = 10 
y = 20
z = x,y

print(z)

# after swapping 
x = 10
y = 20
z = y,x

print(z)

# solution using funtion 
# befor swapping 
def swapping_variable(x,y):
    print("Befor swapping")
    print("x=", x)
    print("y=",y)
        
#after swapping 
    x,y=y,x
    print("After swapping")
    print("x=",x)
    print("y=",y)
    
swapping_variable(10,20)

# method one requiring the user to enter variable
x =int(input("enter the value of x:"))
y = int(input("enter the value of y:"))
print("the value of x and y before swapping is", x,y)
swap=x
x=y
y=swap
print("The value of x is:", x)
print("The value of x is:", x)

# method 3: using the funtion
def swap_value(x,y):
    swap = x
    x = y
    y = swap
    return x,y
print(swap_value)
int(input("enter the value of x for method 3:")),
int(input("enter the value of y for method 3:"))
