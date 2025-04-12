import random

#Goal 1
def rand1(i):
    num = random.randrange(0, i)
    return num

randomnum = rand1(5)
print(randomnum)

#Goal 2
def rand2(a, b):
    num2 = random.randint(a, b)
    return num2

randomnum2 = rand2(2, 6)
print(randomnum2)

#Goal 3
def rand1(i):
    num3 = random() * i
    return num3

randomnum3 = rand1(5)
print(randomnum3)

#Challenge 1
def roll_2_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    return total

total = roll_2_dice()
print(total)

#Challenge 2
def shuffle(list):
    i = random.randint(0, len(list))
    chosen = list[i]
    return chosen

chosen = shuffle(["World's Smallest Violin", "Karma", "Bang!", "Inertia", "My Play"])
print(chosen)

#Challenge 3
def x_sided_dice(x):
    num4 = random.randint(1, x)
    return num4

randomnum4 = x_sided_dice(7)
print(randomnum4)