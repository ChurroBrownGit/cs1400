distance = float(input("How long do you have to travel? (In miles): "))
sunny = input("Is it sunny?: ").lower
if sunny == "yes" or sunny == "y":
    is_sunny = True
else:
    is_sunny = False
bike = input("Do you own a bike?: ").lower
if bike == "yes" or bike == "y":
    owns_bike = True
else:
    owns_bike = False
rush_hour = input("Is it currently rush hour?: ").lower
if rush_hour == "yes" or rush_hour == "y":
    is_rush_hour = True
else:
    is_rush_hour = False
car = input("Do you own a car?: ").lower
if car == "yes" or car == "y":
    owns_car = True
else:
    owns_car = False

if distance < 5.0:
    if is_sunny == True:
        print("I recommend walking!")
    else:
        print("I recommend driving!")
if distance >= 5.0 and distance <= 20.0:
    if owns_bike == True:
        print("I recommend cycling!")
    else:
        print("I recommend taking the bus!")
if distance > 20.0:
    if owns_bike == True and rush_hour == False:
        print("I recommend driving!")
    elif rush_hour == True:
        print("I recommend taking the train!")