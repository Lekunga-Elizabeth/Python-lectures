#functions withou parameter
#example 1

def my_name():
    print('welcome to america elizabeth')
my_name()

#example 2
def my_profession():
    print("DevOps Engeer")
my_profession()

# funtion with paramenter
# example 1
def course_func(name,age):
    print("my name is",name,"i am age",age, "old")
course_func("elizabeth", 10)

#example 2
def my_credentials(name,address,birthday):
    print("my name is",name,"i live in ", address, "i was born on ",birthday,)
my_credentials("elizabeth","maryland","january 15th 1990")

#example 3
def even_odd(number):
    if number % 2==0:
        print("is even number", number)
    else:
        print("is an odd number", number)
even_odd(8)

# example 4
def checkdivisibility(a,b):
    if a%b ==0:
        print("is it divisible", a)
    else:
        print("it is not divisible",b)
checkdivisibility(25,6)
        