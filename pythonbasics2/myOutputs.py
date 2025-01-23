#Goal 1
name = "Joel"
age = "16"
print(name, "is", age, "years old!")

#Goal 2
print("My name is", end=" ")
print("Joel!")

#Challenge 1
def hyphenate(words):
    print(*words, end= " ", sep="-")

words = input("What is your string?").split()
hyphenate(words)

#Challenge 2
def repeater(word, number):
    for num in range(0, number):
        print(word)

word = input("What is the word?")
number = int(input("What is the number?"))
repeater(word, number)