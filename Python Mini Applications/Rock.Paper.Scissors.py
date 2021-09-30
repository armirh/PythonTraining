# rock paper scissors game

import random

while True:
    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)
    player = None

    while player not in choices:  # so we pick one of the choices, not just random stuff
        player = input("Rock, paper or scissors?: ").lower()  # .lower, we can put input in lowercase doesn't matter

    if player == computer:
        print('Computer: ', computer)
        print('Player: ', player)
        print("That is a tie!")
    elif player == "rock":
        if computer == "paper":
            print('Computer: ', computer)
            print('Player: ', player)
            print("You lose!")
        if computer == "scissors":
            print('Computer: ', computer)
            print('Player: ', player)
            print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print('Computer: ', computer)
            print('Player: ', player)
            print("You lose!")
        if computer == "paper":
            print('Computer: ', computer)
            print('Player: ', player)
            print("You win!")
    elif player == "paper":
        if computer == "scissors":
            print('Computer: ', computer)
            print('Player: ', player)
            print("You lose!")
        if computer == "rock":
            print('Computer: ', computer)
            print('Player: ', player)
            print("You win!")

    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Goodbye!")
