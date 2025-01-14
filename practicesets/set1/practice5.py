year = int(input("Name a random year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("This is a leap year.")
else:
    print("This isn't a leap year.")
