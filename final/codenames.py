#CODENAMES
#Rob Combs, Joel Hadley, Zach Sherratt

#GAMEPLAN:
#Step 3: Play
    #-Who goes first?
    #-Assign 2 people to a turn
    #-Give hint
    #-Guess
    #-Correct or Incorrect?
#Step 4: Winner
    #-Which team found all agents
    #-End game


import random
import os

def makeboard(filename):
    codewords1 = []
    codewords2 = []
    codewords3 = []
    codewords4 = []
    codewords5 = []
    with open(filename, "r") as file:
        words = file.readlines()
        words = [word.strip() for word in words]
        codewords1 = random.sample(words, 5)
        print(codewords1)
        codewords2 = random.sample(words, 5)
        print(codewords2)
        codewords3 = random.sample(words, 5)
        print(codewords3)
        codewords4 = random.sample(words, 5)
        print(codewords4)
        codewords5 = random.sample(words, 5)
        print(codewords5)

newwordboard = makeboard("codenames.txt")

def spyboard():
    num_blue = random.choice([8, 9])
    num_red = 17 - num_blue
    num_assassin = 1
    num_civilian = 25 - (num_blue + num_red + num_assassin)
    roles = ["B"] * num_blue + ["R"] * num_red + ["C"] * num_civilian + ["A"]
    random.shuffle(roles)
    return roles, num_blue

def print_board(board):
    for i in range(0, 25, 5):
        print(board[i:i+5])

newspyboard, num_blue = spyboard()

def players(num_blue):
    numofplayers = int(input("How many players will be playing?: "))
    if numofplayers > 8:
        print("fuck you")
    else:
        names = []
        first = "0"
        for i in range(numofplayers):
            name = input("What is thou name?: ")
            names.append(name)
        random.shuffle(names)
        half = numofplayers // 2
        teamred = names[:half]
        teamblue = names[half:]
        if num_blue == 8:
            first = "Red"
        elif num_blue == 9:
            first = "Blue"
    return teamred, teamblue, first

teamblue, teamred, first = players(num_blue)
print("Team 1:", teamred)
print("Team 2:", teamblue)
print("Team " + first + " will go first.")

def turns(newspyboard, teamblue, teamred): 
    guesserblue = random.choice(teamblue)
    teamblue.remove(guesserblue)
    codegivblue = random.choice(teamblue)
    teamblue.append(guesserblue)
        
    guesserred = random.choice(teamred)
    teamred.remove(guesserred)
    codegivred = random.choice(teamred)
    teamred.append(guesserred)
    
    return guesserred, guesserblue, codegivred, codegivblue
    
guesserred, guesserblue, codegivred, codegivblue = turns(newspyboard, teamblue, teamred)
print("Team Red's guesser is " + str(guesserred) + ".")
print("Team Blue's guesser is " + str(guesserblue) + ".")
print("Team Red's codegiver is " + str(codegivred) + ".")
print("Team Blue's codegiver is " + str(codegivblue) + ".")

def play(newspyboard, teamblue, teamred, gusserred, guesserblue, first, newwordboard, codgivred, codgivblue):
    #chicken jockey
    print("pls have everyone but the code givers to look away, when your ready to proceed and see the spyboard please press 1")
    answer=int(input("pls for the love of everything thats holy press 1"))
    if answer==1:
        print(spyboard)
    else:
        print("what you mean by that?!")

