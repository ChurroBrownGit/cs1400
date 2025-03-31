import random

#Goal 1
count = 0
while count < 20:
    count += 1

print(count)

#Goal 2
userimput = "go"

while userimput.lower() != "stop":
    print("Hello")
    userimput = input("Input the keyword: ")

#Goal 3
num = 10
total = 0

while num < 21:
    total = total + num
    num += 1

print(total)

#Challenge 1
def bananas(numba):
    totals = 0
    while totals < numba:
        print("banana")
        totals += 1

numba = int(input("How many times would you like to print?: "))
bananas(numba)

#Challenge 2
def hit_me(total):
    hitme = True
    while hitme == True:
        answer = input("Do you want to hit again?: ")
        if answer.lower() == "yes":
            total += random.randint(0,6)
        else:
            return total
            hitme = False

hit_me(0)
print(total)

#Challenge 3
repeat = True
while repeat == True:
    print("rinse and repeat")
    # You can end the program by putting "repeat = False" after the print statement.