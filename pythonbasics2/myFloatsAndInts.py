#Goal 1
def burritos_for_each(burritos, people):
    burritos_per_person = 0
    burritos_per_person = burritos_per_person + burritos // people
    return (burritos_per_person)

burritos = 39
people = 7
burritos_per_person = burritos_for_each(burritos, people)
print(burritos_per_person)

#Goal 2
def give_me_5(num):
    num = num + 5
    return num

num = int(input("What is the number?"))
num = give_me_5(num)
print(num)

#Goal 3
def chop(number):
    number = number - int(number)
    return number

number = float(input("What float do you choose? "))
number = chop(number)
print(number)

#Challenge 1
def roundup(number2):
    number2 = number2 + 1
    number2 = number2 // 1
    return number2

number2 = float(input("What float number? "))
number2 = roundup(number2)
print(number2)

#Challenge 2
def quotient(float1,float2):
    factor = 100
    float1 = float1 * factor
    float2 = float2 * factor
    quotients = float1 // float2
    return quotients * 0.01

float1 = float(input("What float number? "))
float2 = float(input("What float number? "))
quotients = roundup(float1,float2)
print(quotients)