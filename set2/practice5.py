score = int(input("What was the student's score?: "))
participation = input("What was the student's participation level? (excellent, above average, average, poor): ").lower
homework = input("Was all homework completed?: ").lower
if homework == "yes" or homework == "y":
    homework_completed = True
else:
    homework_completed = False

if score >= 90:
    if participation == "excellent":
        print("This grade is A+")
    else:
        print("This grade is A")
elif score <= 89 and score >= 80:
    if participation == "excellent" or participation == "above average":
        print("This grade is B+")
    else:
        print("This grade is B")
elif score <= 79 and score >= 70:
    if homework_completed == True:
        print("This grade is C+")
    else:
        print("This grade is C")
elif score < 70:
    if participation == "poor":
        print("This grade is F")
    else:
        print("This grade is D")