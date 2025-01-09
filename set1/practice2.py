grade = float(input("What is the grade percent? "))
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
