#Goal 1
def sum(x,y):
    return int(x + y)

x = int(input("What is x?"))
y = int(input("What is y?"))
newsum = sum(x,y)
print(newsum)

#Goal 2
def product(a,b):
    return int(a*b)

a = int(input("What is a?"))
b = int(input("What is b?"))
newproduct = product(a,b)
print(newproduct)

#Goal 3
def at_least_double(r,d):
    return int(r*d)

r = int(input("What is r?"))
d = 2
double = at_least_double(r,d)
print(double)

#Challenge 1
#There is no minimum amount of parameters, as you can do 0 without an error. 
#However, the maximum amount of parameters is 255, otherwise this will overload the argument.

#Challenge 2
def parameter(j):
    if j == 2:
        print("yes")

parameter()
#This gives a TypeError that tells you you are missing a possitional argument.