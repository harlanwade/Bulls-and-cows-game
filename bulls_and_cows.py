"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Kryštof Karel
email: krystof.karel@gmail.com
"""

import random

def generate_number():
    number = str(random.randint(1000, 9999))
    while len(set(number)) != 4:
        number = str(random.randint(1000, 9999))
    return number

def is_valid_guess(guess):
    return len(guess) == 4 and guess.isnumeric() and guess[0] != "0" and len(set(str(guess))) == 4

def count_bulls_and_cows(guess, number):
    number_of_bulls = 0
    number_of_cows = 0
    for i in range(len(guess)):
        if guess[i] in number:
            if guess[i] == number[i]:
                number_of_bulls += 1
            else:
                number_of_cows += 1
    return number_of_bulls, number_of_cows

def play_game():
    print("""
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
""")
    
    number = generate_number()
    guess = input("Enter a number: ")
    attempts = 0

    while guess != number:
        if is_valid_guess(guess):
            number_of_bulls, number_of_cows = count_bulls_and_cows(guess, number)
            bulls = "bull" if number_of_bulls == 1 else "bulls"
            cows = "cow" if number_of_cows == 1 else "cows"
            print(number_of_bulls, bulls, "and", number_of_cows, cows)
            print("""
-----------------------------------------------
""")
        else:
            print("Invalid attempt.")
            print("""
-----------------------------------------------
""")
        guess = input("Enter a number: ")
        attempts += 1
    else:
        attempts += 1
        print(f"Correct, you've guessed the right number in {attempts} guesses!")
        exit()

if __name__ == "__main__":
    play_game()
