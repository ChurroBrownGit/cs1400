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
print_board(newspyboard)

def players(num_blue):
    numofplayers = int(input("How many players will be playing?: "))
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

def turns(newwordboard, newspyboard, teamblue, teamred, first): 
    codegiver = random.randint(teamblue)
    
    for item in teamblue:
        guesser=random.randint(teamblue)
