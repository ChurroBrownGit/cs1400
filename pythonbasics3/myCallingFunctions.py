#Goal 1
def noun(noun_list, num):
    return noun_list[num]

new_nown = noun(["car", "dog", "sheep", "horse"], 3)
print(new_nown)

#Goal 2
def adjective(adjective_list, num2):
    return adjective_list[num2]

new_adjective = adjective(["small", "sweet", "short", "smelly"], 2)
print(new_adjective)

#Goal 3
def silly_sentence():
    print("The " + noun(["car", "dog", "sheep", "horse"], 1) + " was really " + adjective(["small", "sweet", "short", "smelly"], 1))
    
silly_sentence()

#Challenge 1
def main(totalcost, friends):
    tipformeal(totalcost)
    splittingbill(totalcost, friends)

def tipformeal(totalcost):
    tipamount = 0
    tipamount = tipamount + int(totalcost) * 0.15
    print("The tip amount is $" + str(tipamount))

def splittingbill(totalcost, friends):
    eachpersonowes = 0
    eachpersonowes = eachpersonowes + (int(totalcost) / int(friends))
    print("Each person owes $" + str(eachpersonowes))
    
main(150, 3)