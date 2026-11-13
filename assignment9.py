#Robert Fowler
#Assignment 9 - Number Guessing Game

import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0
    guess_history = []
    while guess != number_to_guess:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        guess_history.append(guess)
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
    print("Congratulations! You've guessed the number.")
    print(f"It took you {attempts} guesses.")
    print(f"Your guesses: {guess_history}")

if __name__ == "__main__":
    number_guessing_game()
