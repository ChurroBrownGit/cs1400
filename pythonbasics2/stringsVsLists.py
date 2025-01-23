#Goal 1
alphabet = "abcdefghijklmnopqrstuvwxy"
print(alphabet[0])
print(alphabet[12])
print(alphabet[19])
print(alphabet[26])
#Prints a, m, and t, but index 26 is out of range, because its actually taking letter 27 (which doesn't exist).
#Gives an IndexError.

#Goal 2
strings = "supercalifragilistic"
for i in range(0, len(strings)):
    print(strings[i])
#Prints every letter on a new line.

#Goal 3
string2 = "bananarama"
for i in range(0, len(string2)):
        if i%2==0:
            print(string2[i])

#Challenge 1
def catch_zs(new_string, numberofzs):
    for index in range(len(new_string)):
        if new_string[index] == 'z':
            numberofzs += 1
    return numberofzs

numberofzs = 0
new_string = input("What is the string?")
numberofzs = catch_zs(new_string, numberofzs)
print(numberofzs)

#Challenge 2
def find_x(string3):
    for item in range(len(string3)):
        if string3[item] == 'x':
            return item
    return -1
    
print(find_x(s = input("What is the string?")))