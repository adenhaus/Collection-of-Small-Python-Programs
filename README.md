# A Collection of Short Python Programs

> Miscellaneous small console apps written in Python during the first month that I was learning to code. Nothing super advanced but some are quite fun and document my journey.

#### Files
In this repo you will find:
* **Hang Man** (and words.txt which hang_man.py reads from)
* **Password Generator**
* **Guess the Number**
* **Rock Paper Scissors**

#### App Descriptions
###### Hang Man
This one is actually really fun to play. It chooses a random word from the .txt file, shows you the length by replacing each letter in the word with a * and promts you to make a guess. Each time you make a correct guess that letter will be revealed in the word, for example h*** until you guess them all and see a victory message. You have 10 lives, and if you make 10 mistakes you will see a loss message and the correct word will be revealed.
Possible future improvements: Difficulty selection to choose from shorter or longer words with more or fewer lives.
###### Password Generator
After asking you how long you'd like the password to be, the program generates a secure password using letters, digits and punctuation characters of the selected length.
Possible future improvements: Select if you want letters, digits or punctuation characters.
###### Guess the Number
This one does pretty much what you'd expect. It's a rather insipid game where you guess a number between 1 and 10. The program tells you if you gessed too low or too high and you have 4 chances until you lose and the number is revealed. If you guess it correctly, of course, you win. (The most interesting part for the user is picking a strategy to win. How many chances you you need to be given for it to be possible to win every time? And how should you guess?)
###### Rock Paper Scissors
Just an endless rock, paper, scissors game with the computer. It has error handling for the inputs, as do the rest of the little programs in this repo.

*Version 4.0*
