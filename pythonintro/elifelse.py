#Goal 1

age = int(input("What is your age? "))
if age >= 0 and age <= 12:
    print("You are a child.")
elif age >= 13 and age <= 25:
    print("You are a young adult.")
elif age >= 25:
    print("You are an adult.")

#Goal 2 
def prize():
    spin = int(input("What is your number?: "))
    if spin <= 10:
        print("Your prize is a laptop!")
    elif spin >=11 and spin <=20:
        print("Your prize is a watch!")
    elif spin >=21 and spin <=30:
        print("Your prize is a tablet!")
    elif spin >=31 and spin <=40:
        print("Your prize is a phone!")
    elif spin <=50 and spin >=41:
        print("Your prize is a car!")