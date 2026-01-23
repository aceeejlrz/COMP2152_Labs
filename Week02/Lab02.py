import random
choices = ["Rock", "Paper", "Scissors"]

playerChoice = input("Chose a number between the following list: 1-Rock, 2-Paper, 3-Scissors: ")

playerChoice = int(playerChoice)
# Input check 
if playerChoice < 1 or playerChoice > 3:
    print("Error: You should choose a number between 1 and 3!")
else:
    #Develop the game logic through if/elif/else statements
    computerChoice = random.randint(1, 3)
    if playerChoice == computerChoice:
        print("Tie!")
    elif playerChoice == 1 and computerChoice == 2:
        print("You lose!")
    elif playerChoice == 1 and computerChoice == 3:
        print("You win!")
    elif playerChoice == 2 and computerChoice == 1:
        print("You win!")
    elif playerChoice == 2 and computerChoice == 3:
        print("You lose!")
    elif playerChoice == 3 and computerChoice == 1:
        print("You lose!")
    elif playerChoice == 3 and computerChoice == 2:
        print("You win!")