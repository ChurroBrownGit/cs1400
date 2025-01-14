import random

playerschoice = input("Rock, Paper, or Scissors? ")
possilbe_choice = ["Rock", "Paper", "Scissors"]
computerschoice = random.choice(possilbe_choice)

print("You chose " + playerschoice + ".")
print("The computer chose " + computerschoice + ".")

if playerschoice.lower() == "rock" and computerschoice == "Paper" or playerschoice.lower() == "paper" and computerschoice == "Scissors" or playerschoice.lower() == "scissors" and computerschoice == "Rock":
    print("You lost.")
elif playerschoice.lower() == "rock" and computerschoice == "Rock" or playerschoice.lower() == "paper" and computerschoice == "Paper" or playerschoice.lower() == "scissors" and computerschoice == "Scissors":
    print("You tied.")
else:
    print("You win!")