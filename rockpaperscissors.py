import random

#create a list of play options
options = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(options)
player = ""

while player not in options:
    player = input("Enter your choice (Rock/Paper/Scissors): ")

print(f"You chose: {player}")
print(f"The computer chose: {computer_choice}")

if player == computer_choice:
       print ("Deuces!")
elif (player == "Rock" and computer_choice == "Paper") or (player == "Paper" and computer_choice == "Scissors") or (player == "Scissors" and computer_choice == "Rock"):
    print("You are Trash!")
else:
    print ("You are a God!")
       