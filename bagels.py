#Practice using constants
#Deduce a secret three-digit number based on clues

"""Bagels, by AL Sweigart al@invenwithpython.com
A deductive logic game where you must guess a number based on clues.
"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 3

def main():
    print('''Welcome to the Bagels game! 
    I am thinking of a {}-digit number with no repeated digits. 
    Try to guess it, and the clues are :
        1. Close, one digit is correct but in the wrong place.
        2. Yep, one digit is correct and in the right place.
        3. Nope, No digit is correct.'''.format(NUM_DIGITS))

    while True:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print(' You have {} guesses left.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}. '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses. The correct number was {}.'.format(secretNum))

        # Ask player if they want to play again.
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

def getSecretNum():
    '''Returns a string made up of NUM_DIGITS unique random digits.'''
    numbers = list('0123456789') # Create a list of digits 0 to 9
    random.shuffle(numbers) #Shuffle them into random order.

    #Get the first NUM_DIGITS in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += numbers[i]
    return secretNum

def getClues(guess, secretNum):
    '''Returns a string with the clues for a guess and secret number.'''
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Yep')
        elif guess[i] in secretNum:
            clues.append('Close')

    if len(clues) == 0:
        return 'Nope'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()