#Goal 1
from math import *

result1 = sqrt(16)
result2 = factorial(5)
result3 = pi

#Goal 2
from random import randrange

random_number = randrange(0, 13)
print(random_number)

#Goal 3
from math import factorial

result1 = factorial(10)
print(result1)

def factorial(a):
    return "Hello"

result2 = factorial(10)
print(result2)

#The first call will return 3,628,800 but the second call will return "Hello"
#This is caused by the factorial() overriding the already imported factorial().

#Challenge 1
import math

def exp(x):
    return math.exp(x)

result = exp(2)
print(result)
direct_result = math.exp(2)
print(direct_result)