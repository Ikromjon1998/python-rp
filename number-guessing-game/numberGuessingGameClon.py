import random
import math

def get_boundaries():
    '''Prompt the user to enter the lower and upper bounds for the guessing game.'''
    lower = int(input("Enter Lower bound:- "))
    upper = int(input("Enter Upper bound:- "))
    return lower, upper

def random_integer(lower, upper):
    '''Generate random integer between lower and upper bounds.'''
    return random.randint(lower, upper)

def calculate_chances(lower, upper):
    '''Calculate the total number of guesses based on the range size.'''
    # Number of chances is based on the binary logarithm of the range size.
    # The function math.log(x+1, 2) gives the binary logarithm of x+1.
    # Rounding down ensures integer amount of chances.
    return math.floor(math.log(upper - lower + 1, 2))

def guessing_game(x, total_chances):
    '''Main game routine. Prompts the user to guess a number until they run out of chances or choose correctly.'''
    for chance in range(total_chances):
        guess = int(input("Guess a number:- "))

        if guess == x:
            print(f"Congratulations! You guessed the number in {chance + 1} tries.")
            return
        elif guess < x:
            print("You guessed too small!")
        elif guess > x:
            print("You guessed too high!")

    print(f"\nThe number was {x}")
    print("\tBetter luck next time!")

def main():
    lower, upper = get_boundaries()
    x = random_integer(lower, upper)
    total_chances = calculate_chances(lower, upper)
    print(f"You have {total_chances} chances to guess the number between {lower} and {upper}.\n")
    guessing_game(x, total_chances)

# Call the main function to start the game
if __name__ == "__main__":
    main()