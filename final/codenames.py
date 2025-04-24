#CODENAMES
#Rob Combs, Joel Hadley, Zach Sherratt

#GAMEPLAN:
#Step 1: Setup
    #-Make randomized board - DONE
    #-List of codenames - DONE
    #-Random spy location generator - 
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

makeboard("codenames.txt")

def spyboard()

def turns():

