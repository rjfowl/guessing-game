#Robert Fowler
#Assignment 9 - Number Guessing Game

import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    guess = None
    while guess != number_to_guess:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
    print("Congratulations! You've guessed the number.")

if __name__ == "__main__":
    number_guessing_game()