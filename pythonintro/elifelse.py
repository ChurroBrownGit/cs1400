#Goal 1

age = int(input("What is your age? "))
if age >= 0 and age <= 12:
    print("You are a child.")
elif age >= 13 and age <= 25:
    print("You are a young adult.")
elif age >= 25:
    print("You are an adult.")

#Goal 2

def prize(spin):
    if spin <= 10:
        return "Your prize is a laptop!"
    elif spin >=11 and spin <=20:
        return "Your prize is a watch!"
    elif spin >=21 and spin <=30:
        return "Your prize is a tablet!"
    elif spin >=31 and spin <=40:
        return Your prize is a phone!"
    elif spin <=50 and spin >=41:
        return "Your prize is a car!"

spin = int(input("What is your number?: "))
r = prize(spin)
print(r)

#Challenge 1

def fast_food_menu(number)
    if number == 1:
        return "Hamburger"
    if number == 2:
        return "French Fries"
    if number == 3:
        return "Onion Rings"
    if number == 4:
        return "Grilled Cheese"
    if number == 5:
        return "Milkshake"
    if number == 6:
        return "Drink"
    if number > 6:
        return False

number = int(input("What is the menu item number? ")
food = fast_food_menu(number)
print(food)
