total_amount = float(input("What is the total price? "))
total_items = int(input("How many total items? "))
member = input("Are you a member? ").lower
if member == "yes" or member == "y":
    is_member = True
first_time_buyer = input("Are you a first time buyer? ").lower
if first_time_buyer == "yes" or first_time_buyer == "y":
    is_first_time_buyer = True

if total_amount > 200.00:
    if is_member == True:
        total_amount = total_amount * 0.8
        print("Your new total is " + str(total_amount) + ".")
    else:
        total_amount = total_amount * 0.9
        print("Your new total is " + str(total_amount) + ".")
elif total_amount >= 100.00 and total_amount <= 200.00:
    total_amount = total_amount * 0.95
    if total_items > 5:
        total_amount = total_amount - 10
        print("Your new total is " + str(total_amount) + ".")
    else:
        total_amount == total_amount
        print("Your new total is " + str(total_amount) + ".")
elif total_amount < 100:
    if first_time_buyer == True:
        total_amount = total_amount - 5
        print("Your new total is " + str(total_amount) + ".")
    else:
        total_amount == total_amount
        print("Your new total is " + str(total_amount) + ".")