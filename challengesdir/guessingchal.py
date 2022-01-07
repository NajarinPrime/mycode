#!/usr/bin/env python3
"""Number guessing game!"""

import random

def main():
    num= random.randint(1,100)
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 5:
        guess= int(input("Guess a number between 1 and 100"))
        quit= "q"

        if guess > num:
            print("Too high!")
            attempt = attempt + 1

        elif guess < num:
            print("Too low!")
            attempt = attempt + 1

        else:
            print("Correct!")
            still_guessing = False
    if attempt == 5:
        print(f'{num} was the answer')

main()
