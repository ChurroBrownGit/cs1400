#Goal 1
list1 = []
for i in range(10):
    list1.append(i)

#Goal 2
scores = []
for i in range(101):
    scores.append(0)
print(scores)

#Goal 3
def bonus(list2):
    for i in range(len(list2)):
        list2[i] = list2[i] + 50
    print(list2)

list2 = [1, 2, 3, 4, 5, 6, 7, 8]
bonus(list2)

#Challenge 1
def even_bonus(list3):
    for i in range(len(list3)):
        if (i + 1) % 2 == 0:
            list3[i] = list3[i] + 50
    print(list3)

list3 = [1, 2, 3, 4, 5, 6, 7, 8]
even_bonus(list3)

#Challenge 2
def trey_bonus(list4):
    for i in range(len(list4)):
        if (i + 1) % 3 == 0:
            list4[i] = list4[i] + 50
    print(list4)

list4 = [1, 2, 3, 4, 5, 6, 7, 8]
trey_bonus(list4)