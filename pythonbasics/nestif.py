#Goal 1

def carnivalride(height):
    if height < 60:
        if height > 20:
            print("You must ride with a parent!")
        else:
            print("Sorry, you cant ride!")
    else:
        if height < 120:
            print("You can ride alone!")
        else:
            print("Woah, you are a little tall for this ride!")

carnivalride(27)
carnivalride(87)
carnivalride(12)

#Challenge 1

def predictor(num1, num2)
    if num1 % 2 == 0:
        if num2 % 2 == 0:
            return "definitely"
        elif num2 % 2 != 0:
            return "likely"
    elif num1 % 2 != 0:
        if num2 % 2 != 0:
            return "definitely not"
        elif num2 % 2 == 0:
            return "unlikely"

num1 = int(input("Choose a number: ")
num2 = int(input("Choose another number: ")
prediction = predictor(num1, num2)
print(prediction)
