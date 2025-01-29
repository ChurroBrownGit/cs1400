#Goal 1
print("dog" + 55)
#This gives a concatenation TypeError.

#Goal 2
def combine(number, string):
    print(string + str(number))

combine(3, "car")

#Challenge 1
def write_numbers(x):
    f = open("numbers.txt", "a")
    for i in range(0,x + 1):
        i = i * 5
        f.write(str(i))
    f.close()

write_numbers(3)