# Guess the number game
import random

# Generate a random number
num = str(random.randint(1, 10))

# To check if the program is working:
# print(num)

# Request user input
print("Guess a number from 1 to 10, you have 4 chances...")

# Declare counter variables
count = 0
turn = 4

while True:

    guess = input()

    if guess == num:
        print("You win! The number was " + num)
        break

    elif count == 3:
        print("You lose! The number was " + num)
        break

    else:
        turn -= 1

        if turn == 1:
            if int(guess) > int(num):
                print("Your guess was too high. Try again. " + str(turn) + " guess left...")
            elif int(guess) < int(num):
                print("Your guess was too low. Try again. " + str(turn) + " guess left...")

        else:
            if int(guess) > int(num):
                print("Your guess was too high. Try again. " + str(turn) + " guesses left...")
            elif int(guess) < int(num):
                print("Your guess was too low. Try again. " + str(turn) + " guesses left...")
        count += 1
