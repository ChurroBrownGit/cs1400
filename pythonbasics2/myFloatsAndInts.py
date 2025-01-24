#Goal 1
def burritos_for_each(burritos, people):
    burritos_per_person = 0
    burritos_per_person = burritos_per_person + burritos // people
    return (burritos_per_person)

burritos = 39
people = 7
burritos_per_person = burritos_for_each(burritos, people)
print(burritos_per_person)
