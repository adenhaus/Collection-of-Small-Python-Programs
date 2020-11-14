import random

print("HANGMAN")

f = open("words.txt", "r")
a = f.read()
words_list = a.split("\n")

word = random.choice(words_list)
char_list = []
guesses = []

for i in word:
    char_list.append(i)

str_set = set(word)

counter = 0
death_count = 10

while death_count > 0 and counter < len(str_set):

    for i in char_list:
        if i in guesses:
            print(i, end="")
        else:
            print("*", end="")

    if death_count > 1:
        guess = input("\n\nGuess a letter. You have " + str(death_count) + " incorrect guesses: ")
    else:
        guess = input("\n\nGuess a letter. You have " + str(death_count) + " incorrect guess: ")

    if guess in char_list:
        if guess not in guesses:
            guesses.append(guess)
            counter += 1
            print("\nCorrect, that letter is in the word!\n")
        else:
            print("\nYou have already guessed that letter.\n")

    else:
        death_count -= 1
        print("Wrong!")

if death_count == 0:
    print("\nYou lose. The word was " + word)

else:
    print("\nYou win. The word was " + word)
