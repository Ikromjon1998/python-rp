import random
import math

lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))

x = random.randint(lower, upper)

number_of_chances = math.log(upper-lower + 1, 2);

print("\n\tYou've only ",
      round(number_of_chances),
      " chances to guess the integer!\n")

count = 0

while count < number_of_chances:
    count += 1

    guess = int(input("Guess a number: - "))

    if x == guess:
        print("Congratulations you did it in ", count, " try")
        break
    elif x > guess:
        print("You guessed too samll!")
    elif x < guess:
        print("You guessed too high!")

if count >= number_of_chances:
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
