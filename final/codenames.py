#CODENAMES
#Rob Combs, Joel Hadley, Zach Sherratt

#GAMEPLAN:
#Step 1: Setup
    #-Make randomized board
    #-List of codenames
    #-Random spy location generator
#Step 2: Players
    #-Create teams, num of players
    #-Choose names
    #-Choose hint guy and guess guy
#Step 3: Play
    #-Who goes first?
    #-Assign 2 people to a turn
    #-Give hint
    #-Guess
    #-Correct or Incorrect?
    #-Assassin location
#Step 4: Winner
    #-Which team found all agents
    #-End game

import random

def makeboard(filename):
    with open(filename, "r") as file:
        words = file.readlines()
        if words:
            random_word = random.choice(words)
            print(random_word.strip())
        else:
            print("Empty file!")

makeboard("codenames.txt")

def turns():

def spyboard():