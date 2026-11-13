#Robert Fowler
#Assignment 9 - Number Guessing Game

import random

def number_guessing_game(limit):
    number_to_guess = random.randint(1, limit)
    guess = None
    while guess != number_to_guess:
        guess = int(input(f"Guess a number between 1 and {limit}: "))
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
    print("Congratulations! You've guessed the number.")

#Manual Feature
#difficulty setting; changes the range of numbers that can be guessed
#easy 1-10; med 1-100; hard 1-1000
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