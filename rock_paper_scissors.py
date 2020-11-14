import random

print("Type rock, paper, or scissors to make your move, or type stop to exit.")

while True:
    move = random.choice(['rock', 'paper', 'scissors'])
    choice = input()
    choice = choice.lower()

    if choice.lower() == "rock" and move == "scissors":
        print("Your choice: " + choice + "\nThe computer's choice: " + move + "\nYou won!")

    elif choice.lower() == "rock" and move == "rock":
        print("Your choice: " + choice + "\nThe computer's choice: " + move + "\nYou tied!")

    elif choice.lower() == "rock" and move == "paper":
        print("Your choice: " + choice + "\nThe computer's choice: " + move + "\nYou lost!")

    elif choice.lower() == "paper" and move == "scissors":
        print("Your choice: " + choice + "\nThe computer's choice: " + move + "\nYou lost!")

    elif choice.lower() == "paper" and move == "paper":
        print("Your choice: " + choice + "\nThe computer's choice: " + move + "\nYou tied!")

    elif choice.lower() == "paper" and move == "rock":
        print("Your choice: " + choice + "\nThe computer's choice: " + move + "\nYou won!")

    elif choice.lower() == "scissors" and move == "rock":
        print("Your choice: " + choice + "\nThe computer's choice: " + move + "\nYou lost!")

    elif choice.lower() == "scissors" and move == "scissors":
        print("Your choice: " + choice + "\nThe computer's choice: " + move + "\nYou tied!")

    elif choice.lower() == "scissors" and move == "paper":
        print("Your choice: " + choice + "\nThe computer's choice: " + move + "\nYou won!")

    elif choice.lower() == "stop":
        break

    else:
        print(choice + " is not a valid input, try again.")