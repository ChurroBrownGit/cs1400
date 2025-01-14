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