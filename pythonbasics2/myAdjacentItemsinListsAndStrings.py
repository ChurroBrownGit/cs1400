#Goal 1
def double2(list1):
    for i in range(len(list1)):
        if i == 2:
            list1[i] = list1[i] * 2
    print(list1)

list1 = [2, 3, 4, 2, 5, 3, 6, 2, 7]
double2(list1)

#Goal 2
def x_out(sentence):
    new_string = ""
    for i in range(len(sentence)):
        if sentence[i] == "x":
            new_string += " " 
        else:
            new_string += sentence[i]
    return new_string

sentence = "Next box of axes must exit."
new_string = x_out(sentence)
print(new_string)

#Challenge 1
def stuck(list2):
    for i in range(len(list2)):
        if list2[i] == "rock" and list2[i + 1] == "hard place":
            list2.insert(i + 1, "stuck")
        else:
            list2[i + 1]

list2 = ["rock", "hard place", "pillow", "hard place", "feather", "rock", "hard place", "rock"]
stuck(list2)
print(list2)