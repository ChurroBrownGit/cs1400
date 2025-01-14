income = float(input("What is your total yearly income?: "))
married = input("Are you married? ").lower
if married == "yes" or married == "y":
    is_married = True
else:
    is_married = False
dependents = input("Do you have dependents?: ").lower
if dependents == "yes" or dependents == "y":
    has_dependents = True
else:
    has_dependents = False
business = input("Are you a business owner?: ").lower
if business == "yes" or business == "y":
    owns_business = True
else:
    owns_business = False

if income < 30000.00:
    if is_married == True:
        print("Tax is 8%.")
    else:
        print("Tax is 10%.")
elif income >= 30000.00 and income <= 100000.00:
    if has_dependents == True:
        if is_married == True:
            print("Tax is 12%.")
        else:
            print("Tax is 15%.")
    else:
        print("Tax is 18%.")
elif income > 100000.00:
    if owns_business == True:
        print("Tax is 25%.")
    else:
        print("Tax is 28%.")