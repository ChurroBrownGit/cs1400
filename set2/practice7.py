age = int(input("What is your current age?: "))
fitness_level = input("What is your current fitness level? (beginner, intermediate, advanced): ").lower
goal = input("What is your current goal? (strength, cardio, weight loss): ").lower
concerns = input("Do you have any health concerns?: ").lower
if concerns == "yes" or concerns == "y":
    has_health_concerns = True
else:
    has_health_concerns = False

if age < 18:
    if goal == "strength":
        print("I suggest the Youth Strength Program")
    if goal == "cardio":
        print("I suggest the Youth Cardio Plan")
elif age >= 18 and age <= 50:
    if fitness_level == "beginner":
        print("I suggest the Beginner Strength and Cardio")
    else:
        if goal == "weight loss":
            print("I suggest the HIIT and Strength Plan")
        elif goal == "strength":
            print("I suggest the Advanced Strength Program")
elif age > 50:
    if has_health_concerns == True:
        print("I suggest the Gentle Mobility Program")
    else:
        print("I suggest the Active Aging Plan")