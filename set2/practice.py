age = int(input("What is your age? "))
weekend = input("Is it a weekend? ").lower
if weekend == "yes" or weekend == "y":
    is_weekend = True
student = input("Are you a student? ").lower
if student == "yes" or student == "y":
    is_student = True   

if age < 12:
    print("This ticket costs $8.")
if age <= 12 and age <= 17:
    if is_weekend == True:
        print("This ticket costs $12.")
    elif is_weekend == False:
        print("This ticket costs $10.")
if age >= 18 and age <= 64:
    if is_weekend == False and is_student == True:
        print("This ticket costs $12.")
    else:
        print("This ticket costs $15.")
if age >= 65:
    print("This ticket costs $10.")