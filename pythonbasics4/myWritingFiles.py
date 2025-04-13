#Goal 1
name = "Joel"
myfile = open("myfile.txt", "w")
myfile.write(name+"\n")
myfile.close()
#This file gets put in the main user directory

#Goal 2
things = ["Family", "Friends", "Video Games", "Sleep", "Food"]
myfile = open("myfile.txt", "w")
for thing in things:
    myfile.write(thing +"\n")
myfile.close()

#Challenge 1
def all_my_favorite_things(filename):
    loop = True
    things = []
    while loop == True:
        answer = input("What are your favorite things? ")
        if answer == "stop":
            myfile.close()
            loop = False
            
        else:
            answer.append(things)
            myfile = open("myfile.txt", "w")
            for thing in things:
                myfile.write(thing +"\n")
    myfile.close()