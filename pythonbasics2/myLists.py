#Goal 1
animals = ["dog", "cat", "bird", "horse", "hamster", "cow", "sheep", "goat", "snake", "turtle"]

#Goal 2
print(animals[4], animals[9])

#Goal 3
for item in range(len(animals)):
    print(animals[item])

#Challenge 1
def printCustomers(customers):
    for i in range(len(customers)):
        print(i + 1, ".", customers[i])

customers = ["Alice", "Jeff", "Bob", "Tom"]
printCustomers(customers)

#Challenge 2
def tagAlong(guest_list):
    name = "Joel"
    guest_list.append(name)
    print(guest_list)

guest_list = ["Alice", "Jeff", "Bob", "Tom"]
tagAlong(guest_list)

#Challenge 3
def bigPointTotal(points):
    list2 = []
    for i in range(len(points)):
        if points[i] > 100:
            list2.append(points[i])
    finallist = sum(list2)
    print(finallist)

points = [93, 99, 102, 110, 108, 90]
bigPointTotal(points)