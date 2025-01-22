number = input(int("Input Number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

grade = input(float("What is the grade percent? "))
if grade > 90.0:
    print("This grade is A")
if grade < 89.9 and grade > 80.0:
    print("This grade is B")
if grade < 79.9 and grade > 70.0:
    print("This grade is C")
if grade < 69.9 and grade > 60.0:
    print("This grade is D")
if grade < 60.0:
    print("This grade is F")

integer = input(int("Give a number: "))
if integer > 0:
    print("This number is positive.")
if integer == 0:
    print("This number is zero.")
if integer < 0:
    print("This number is negative.")