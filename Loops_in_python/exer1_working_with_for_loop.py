# in Loops we have two main types that is the For Loop and While Loops 
# the main different is that the for loop is used when the number of iteration is know with the while loops it comes in when the number of iteration is not known 

# How to write a For Loop in python
for num in range(1,11): # here your result will print (o-9)
    print(num)
    
# example2 (in case of a string use i)
name="Lekunga"
for i in name:
    print(i)

#looping with List (we use square bracket to list in all our iterms sperated by commas, with open quatotion for each iterm this in case of string[])
student=['akum', 'lekunga','happiness','richard']
for i in student:
    print(i)

ages=[1,2,3,4,5]
for i in ages:
    print(i)

# using the conditional statement 
for i in student:
    print(i)
for i in ages:
    if i==4:
        print('hey welcome')
    else:
        print('welcome')
# propose a script that print number from 1-20 using the for loop
for num in range(1,21):
    print(num)
    
# performing sum of first 10 numbers using loops (0 to 9)
sum=0
for i in range(1,10):
    sum = sum+i
print('the sum of the numbers is', sum)

#exer2 (sum from 1 to 21)
sum = 1
for i in range(1,21):
    sum = sum+i
print('the sum of the number is',sum)

#exer3 working with condition (print even numbers and odd numbers 0 to 10)
for i in range(1,11):
    if i % 2 ==0:
        print("even number:",i)
    else:
        print('odd number:',i)


