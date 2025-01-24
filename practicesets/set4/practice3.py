age = int(input("Enter your age: "))
smoker = input("Are you a smoker? (yes/no): ").lower()
bmi = float(input("Enter your BMI: "))
exercise = input("Do you exercise regularly? (yes/no): ").lower()

#Unnested (original)
if (age > 50 and smoker == "yes" and bmi > 30 and exercise == "no") or \
   (age > 40 and smoker == "yes" and bmi > 25 and exercise == "no") or \
   (age > 30 and smoker == "no" and bmi < 25 and exercise == "yes") or \
   (age < 30 and smoker == "no" and bmi < 20 and exercise == "yes"):
    print("Your insurance premium is high.")
else:
    print("Your insurance premium is low.")

#Nested
if age > 50:
    if smoker == "yes":
        if bmi > 30:
            if exercise == "no":
                print("Your insurance premium is high.")
            else:
                print("Your insurance premium is low.")
if age > 40:
    if smoker == "yes":
        if bmi > 25:
            if exercise == "no":
                print("Your insurance premium is high.")
            else:
                print("Your insurance premium is low.")
if age > 30:
    if smoker == "no":
        if bmi < 25:
            if exercise == "yes":
                print("Your insurance premium is high.")
            else:
                print("Your insurance premium is low.")
if age < 30:
    if smoker == "no":
        if bmi < 20:
            if exercise == "yes":
                print("Your insurance premium is high.")
            else:
                print("Your insurance premium is low.")
else:
    print("Your insurance premium is low.")
    