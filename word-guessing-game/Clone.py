import random


def get_name():
    # Function to get the user's name
    your_name = input("What is your name? ")
    print("Good Luck ! ", your_name)
    return your_name


def choose_word():
    # Function to choose the random word
    words = ['rainbow', 'computer', 'science', 'programming',
             'python', 'mathematics', 'player', 'condition',
             'reverse', 'water', 'board', 'geeks']

    random_word = random.choice(words)
    return random_word


def check_characters(your_name, random_word):
    # Function to check a user's guesses against the chosen word
    print("Guess the characters")
    guesses = ''
    turns = 12

    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end=" ")
            else:
                print("_", end=" ")
                failed += 1

        if failed == 0:
            print("\nYou Win, " + name)
            print("The word is: ", word)
            return

        guess = input("\nguess a character:")
        guesses += guess

        if guess not in word:
            turns -= 1
            print("\nWrong")
            print("You have", turns, 'more guesses left')
            if turns == 0:
                print("You Lose")
                return


if __name__ == '__main__':
    name = get_name()
    word = choose_word()
    check_characters(name, word)
