temperature = float(input("What is the current temperature in degrees (Fahrenheit)?: "))
raining = input("Is it currently raining?: ").lower
if raining == "yes" or raining == "y":
    is_raining = True
else:
    is_raining = False
windy = input("Is it currently windy?: ").lower
if windy == "yes" or windy == "y":
    is_windy = True
else:
    is_windy = False
time_of_day = input("What is the current time of day? (morning, afternoon, evening): ").lower

if temperature < 50.0:
    if is_raining == True:
        print("I suggest wearing a heavy coat and bringing an umbrella!")
    elif is_windy == True:
        print("I suggest wearing a windbreaker and gloves!")
    else:
        print("I suggest wearing a jacket and scarf!")
elif temperature >= 50 and temperature <= 70:
    if time_of_day == "morning":
        print("I suggest wearing a light jacket!")
    elif time_of_day == "afternoon":
        print("I suggest wearing a long-sleeve shirt!")
    elif time_of_day == "evening" and is_windy == True:
        print("I suggest wearing a sweater and scarf!")
elif temperature > 70:
    if is_raining == True:
        print("I suggest wearing a raincoat and breathable clothes!")
    else:
        print("I suggest wearing a T-shirt and shorts!")