#Practice using constants
#Deduce a secret three-digit number based on clues

"""Bagels, by AL Sweigart al@invenwithpython.com
A deductive logic game where you must guess a number based on clues.
"""

import random

num_digits = 3
max_guesses = int(input("How many guesses would you like? "))

def main():
    print("Welcome to the guessing game! Try to guess the {}-digit in {} tries".format(num_digits, max_guesses))

    while True:
        secretNum = getSecretNum() #'123'
        print('I have thought up a number')

        numGuesses = 1
        while numGuesses <= max_guesses:
            guess = ''
            while len(guess) != num_digits or not guess.isdecimal():
                print('Guess # {}. '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > max_guesses:
                print('You ran out of guesses. The secret number was: {}'.format(secretNum))

            # Ask player if they want to play again.
        print('Do you want to play again? (y/n)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thankyou for playing!')

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(num_digits):
        secretNum += numbers[i]
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Yep')
        elif guess[i] in secretNum[i]:
            clues.append('Oops')

    if len(clues) == 0:
        return 'Nope'
    else:
        clues.sort()
        return ' '.join(guess)

if __name__ == '__main__':
    main()