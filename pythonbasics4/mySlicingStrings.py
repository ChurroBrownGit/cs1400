#Goal 1
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet[::3])

#Goal 2
def everyOther(lst):
    total = 0
    for i in lst[::2]:
        total += i
    return total

print(everyOther([1, 2, 3, 4, 5, 6, 7, 8]))

#Goal 3
def vegetarian(foods):
    return foods[2::3]

print(vegetarian(['hotdog', 'hamburger', 'carrots', 'chicken','bacon', 'celery']))

#Challenge 1
def animorph(str1, str2):
    newstr = str1[:3] + str2[3:]
    return newstr

print(animorph("Lion", "Tiger"))

#Challenge 2
def pigify(word):
    return word[1:] + word[0] + "ay"

print(pigify("stupid"))