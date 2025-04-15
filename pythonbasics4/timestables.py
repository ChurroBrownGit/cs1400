#Goal 1
def choose_number():
    return int(input("Choose a number!: "))

choose_number()

#Goal 2
def ask_problems(number):
    for i in range(13):
        while True:
            user_answer = int(input("What is " + str(number) + " * " + str(i) + "?"))
            correct_answer = number * i
            if user_answer == correct_answer:
                print("Correct!")
                break
            else:
                print("Incorrect, try again.")

ask_problems(7)

#Goal 3
import time

def time_report(start, end):
    time_taken = end - start
    print(f"Time taken: {time_taken} seconds")
    if time_taken < 5:
        print("You finished really fast!")
    elif 5 <= time_taken < 10:
        print("Nice job, you were pretty quick!")
    else:
        print("It took you a bit longer, but that's okay!")

start_time = time.time()
time.sleep(3)
end_time = time.time()

time_report(start_time, end_time)

#Challenge 1
import random

def ask_problems(number):
    multipliers = random.sample(range(13), 12) #Looked this up, but it helped a lot.
    for randommult in multipliers:
        while True:
            user_answer = int(input("What is " + str(number) + " * " + str(randommult) + "? "))
            correct_answer = number * randommult
            if user_answer == correct_answer:
                print("Correct!")
                break 
            else:
                print("Incorrect, try again.")

ask_problems(7)