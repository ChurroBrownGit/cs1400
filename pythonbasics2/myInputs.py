#Goal 1
name = input("What is your name")
print(name)
print(name)
print(name)
print(name)
print(name)
print(name)
print(name)
print(name)
print(name)
print(name)

#Goal 2
def userwords():
    my_list = []
    word1 = input("Enter a word: ")
    my_list.append(word1)
    word2 = input("Enter a word: ")
    my_list.append(word2)
    word3 = input("Enter a word: ")
    my_list.append(word3)
    word4 = input("Enter a word: ")
    my_list.append(word4)
    word5 = input("Enter a word: ")
    my_list.append(word5)
    word6 = input("Enter a word: ")
    my_list.append(word6)
    word7 = input("Enter a word: ")
    my_list.append(word7)
    word8 = input("Enter a word: ")
    my_list.append(word8)
    word9 = input("Enter a word: ")
    my_list.append(word9)
    word10 = input("Enter a word: ")
    my_list.append(word10)
    return my_list

my_list = userwords()
print(my_list)

#Goal 3
def math():
    q1 = int(input("What is 1 + 1?"))
    if q1 == 2:
        print("Correct!")
    else:
        print("Incorrect.")
    q2 = int(input("What is 3 * 9?"))
    if q2 == 27:
        print("Correct!")
    else:
        print("Incorrect.")
    q3 = int(input("What is 16 - 9?"))
    if q3 == 7:
        print("Correct!")
    else:
        print("Incorrect.")
    q4 = int(input("What is 27 - 12?"))
    if q4 == 15:
        print("Correct!")
    else:
        print("Incorrect.")
    q5 = int(input("What is 67 + 32?"))
    if q5 == 99:
        print("Correct!")
    else:
        print("Incorrect.")
    q6 = int(input("What is 8 * 11?"))
    if q6 == 88:
        print("Correct!")
    else:
        print("Incorrect.")
    q7 = int(input("What is 36 / 12?"))
    if q7 == 3:
        print("Correct!")
    else:
        print("Incorrect.")
    q8 = int(input("What is 3 + -2?"))
    if q8 == 1:
        print("Correct!")
    else:
        print("Incorrect.")
    q9 = int(input("What is 14 * 5?"))
    if q9 == 70:
        print("Correct!")
    else:
        print("Incorrect.")
    q10 = int(input("What is 64 / 8?"))
    if q10 == 8:
        print("Correct!")
    else:
        print("Incorrect.")

math()

#Challenge 1
def guess_the_number(numb1):
    numb2 = int(input("What is your guess?"))
    if numb2 == numb1:
        print("Correct!")
    else:
        print("Incorrect.")
        guess_the_number(numb1)

numb1 = 34
guess_the_number(numb1)

#Challenge 2
def average():
    scores = []
    run = True
    while run == True:
        score = input("Input a number: ")
        if score.lower() == "stop":
            averages = sum(scores) / len(scores)
            print(averages)
            run = False
        else:
            scores.append(int(score))
            run = False
            run = True

average()