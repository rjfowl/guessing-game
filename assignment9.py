#Robert Fowler
#Assignment 9 - Number Guessing Game

import random

def number_guessing_game(limit):
    number_to_guess = random.randint(1, limit)
    guess = None
    attempts = 0
    guess_history = []
    while guess != number_to_guess:
        guess = int(input(f"Guess a number between 1 and {limit}: "))
        attempts += 1
        guess_history.append(guess)
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
    print("Congratulations! You've guessed the number.")
    print(f"It took you {attempts} guesses.")
    print(f"Your guesses: {guess_history}")

#Manual Feature
difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
if difficulty == "easy":
    limit = 10
elif difficulty == "medium":
    limit = 100
elif difficulty == "hard":
    limit = 1000
else:
    print("Invalid difficulty. Please choose easy, medium, or hard.")
    limit = None

if __name__ == "__main__":
    if limit is not None:
        number_guessing_game(limit)
