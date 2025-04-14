#Goal 1
while True:
    print("Running...")
    ans = int(input())
    if ans == 0:
        break
print("Goodbye")

#Goal 2
numbers = [1, 3, 5, 7, 2, 4, 6]
total = 0

for num in numbers:
    if num >= 5:
        continue
    total += num
print(total)

#Challenge 1
import random
def secret_number():
    num = random.randint(1,100)
    while True:
        guess = int(input("Guess the number: "))
        if guess == num:
            print("Congratulations") 
            break
    