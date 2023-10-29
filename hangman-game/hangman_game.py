# importing the time module
import time
import random

# welcoming the user
name = input("What is your name? ")

print("Hello, " + name, "Let's play hangman!")

# wait for 1 second
time.sleep(1)

print("Start guessing...")
time.sleep(0.5)

# Here we set the secret word
words = ['apple', 'banana', 'mango', 'strawberry', 'orange', 'grape', 'pineapple']
word = random.choice(words)
guesses = ''

# determine the number of turns
turns = len(word) + 2

while turns > 0:
    # make a counter that starts with zero
    fails = 0

    # for every character in secret_word
    for char in word:
        # see if the character is in the players guess
        if char in guesses:
            # print then out the character
            print(char, end=" ")
        else:
            # if not found, print a dash
            print("_", end=" ")
            # and increase the failed counter with one
            fails += 1
    if fails == 0:
        print("\nYou won")
        print("The word is:", word)
        break

    # ask the user go guess a character
    guess = input("\n\nguess a character: ")

    # set the players guess to guesses
    guesses += guess

    # if the guess is not found in the secret word
    if guess not in word:

        # turns counter decreases with 1 (now 9)
        turns -= 1

        # print wrong
        print("\nWrong")

        # show the number of turns left for the user
        print("You have", + turns, 'more guesses!')

        if turns == 0:
            print("\nYou Lost")
            print("The word was:", word)