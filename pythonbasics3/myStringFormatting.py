#Goal 1
def name():        
    name = input("What is your name? ")
    str = "Welcome %s! Have a wonderful day!" % (name)
    print(str)

name()

#Goal 2
def product(item, inventory):        
    str = "The %s product has %s items availiable for purchase!" % (item, inventory)
    print(str)

product("Plunger" , "3")

#Goal 3
def name():        
    name = input("What is your name? ")
    str = "Welcome " + name + "! Have a wonderful day!"
    print(str)

name()

def product(item, inventory):        
    str = "The " + item + " product has " + inventory +" items availiable for purchase!"
    print(str)

product("Plunger" , "3")

#Challenge 1
def product(items, inventories):        
    for i in range(len(items)):
        str = "The %s product has %s items availiable for purchase!" % (items[i], inventories[i])
        print(str)

product(["Plunger", "Toilet Paper", "Toilet Brush"] , ["3", "4", "2"])