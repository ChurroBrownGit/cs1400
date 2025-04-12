import time

#Goal 1
#This gives a time in seconds and changes every millionth of a second.

#Goal 2
#ctime will match the clocks on your computer/timezone.

#Goal 3
def quiz():
    num1 = 7
    num2 = 3
    correct_answer = num1 + num2
    print("What is", num1, "+", num2, "?")
    start = time.time()
    user_input = int(input("Your answer: "))
    end = time.time()
    total_time = end - start
    if user_input == correct_answer:
        print(total_time)
    
timer = quiz()
print(timer)