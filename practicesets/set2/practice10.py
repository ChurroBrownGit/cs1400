income = float(input("What is your total yearly income?: "))
credit_score = int(input("What is your current credit score? (300-850): "))
collateral = input("Do you have collateral? ").lower
if collateral == "yes" or collateral == "y":
    has_collateral = True
else:
    has_collateral = False
loan_amount = float(input("What is the requested loan amount?: "))


if credit_score > 750:
    if income > 50000:
        print("Loan approved, 5 percent interest rate.")
    else:
        print("Loan approved, 7 percent interest rate.")
elif credit_score >= 600 and credit_score <= 750:
    if collateral == True:
        print("Loan approved, 10 percent interest rate.")
    else:
        print("Loan denied.")
elif credit_score < 600:
    print("Loan denied.")