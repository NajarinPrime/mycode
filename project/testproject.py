#!/usr/bin/env python3
def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Correct Answer')
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('Sorry wrong answer. Try again')
            attempt = attempt + 1
    if attempt == 3:
        print('The correct answer is' + answer)
score = 0
print('Guess the animal')
guess1 = input('Which bear lives at the North Pole?')
check_guess(guess1, 'polar bear')
guess1 = input('Which bear lives at the North Pole?')
check_guess(guess1, 'polar bear')
guess1 = input('Which bear lives at the North Pole?')
check_guess(guess1, 'polar bear')

print('Your score is' + str(score))
