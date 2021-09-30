# Algorithm:
# Below are the Steps: User inputs the lower bound and upper bound of the range. The compiler generates a
# random integer between the range and store it in a variable for future references. For repetitive guessing,
# a while loop will be initialized. If the user guessed a number which is greater than a randomly selected number,
# the user gets an output “Try Again! You guessed too high“ Else If the user guessed a number which is smaller than a
# randomly selected number, the user gets an output “Try Again! You guessed too small” And if the user guessed in a
# minimum number of guesses, the user gets a “Congratulations! ” Output. Else if the user didn’t guess the integer in
# the minimum number of guesses, he/she will get “Better Luck Next Time!” output.

import random
import math

while True:
    # Taking Inputs
    lower = int(input("Enter Lower bound:- "))

    # Taking Inputs
    upper = int(input("Enter Upper bound:- "))

    # generating random number between
    # the lower and upper
    x = random.randint(lower, upper)
    print("\n\tYou've only ",
          round(math.log(upper - lower + 1, 2)),
          " chances to guess the integer!\n")

    # Initializing the number of guesses.
    count = 0

    # for calculation of minimum number of
    # guesses depends upon range
    while count < math.log(upper - lower + 1, 2):
        count += 1

        # taking guessing number as input
        guess = int(input("Guess a number:- "))

        # Condition testing
        if x == guess:
            print("Congratulations you did it in ",
                  count, " try")
            # Once guessed, loop will break
            break
        elif x > guess:
            print("You guessed too small!")
        elif x < guess:
            print("You Guessed too high!")

    # If Guessing is more than required guesses,
    # shows this output.
    if count >= math.log(upper - lower + 1, 2):
        print("\nThe number is %d" % x)

    play_again = input("Do you want to play again? (yes or no): ").lower()

    if play_again != "yes":
        break

print("Good bye!")
