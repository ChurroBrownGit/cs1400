nights = int(input("How many nights are you staying? "))
weekend = input("Is it a weekend? ").lower
if weekend == "yes" or weekend == "y":
    is_weekend = True
else:
    is_weekend = False
room_type = input("What is the room type? (standard, deluxe, suite): ").lower
membership = input("Do you own a membership? ").lower
if membership == "yes" or membership == "y":
    has_membership = True
else:
    has_membership = False

standard = 100.00 * nights
deluxe = 150.00 * nights
suite = 250.00 * nights

if is_weekend == True:
    standard = standard + (20.00 * nights)
    deluxe = deluxe + (20.00 * nights)
    suite = suite + (50.00 * nights)
elif has_membership == True:
    standard = standard * 0.90
    deluxe = deluxe * 0.90
    suite = deluxe * 0.90
elif nights > 5:
    standard = standard * 0.95
    deluxe = deluxe * 0.95
    suite = suite * 0.95

print("The standard price total is: " + str(standard))
print("The deluxe price total is: " + str(deluxe))
print("The suite price total is: " + str(suite))