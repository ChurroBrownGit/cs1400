number = int(input("Name a number: "))
if number == 0 or number == 10 or number > 0 and number < 10:
    print("This is in the range of 1-10.")
if number == 11 or number == 20 or number > 11 and number < 20:
    print("This is in the range of 11-20.")
if number > 20:
    print("This number is out fo the ranges.")