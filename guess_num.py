import random

def askForGuess():
    guess = input('> ')

    if guess.isdecimal():
        return int(guess)
    print('Please enter a number between 1 and 100')

print('Guess the number')
secretNumber = random.randint(1, 100)

for i in range(10):
    print('You have {} guesses left.'.format(10 - i))
    guess = askForGuess()
    if guess == secretNumber:
        print('Correct!')
        break
    #offer a hint
    elif guess < secretNumber:
        print('Too low!')
    elif guess > secretNumber:
        print('Too high!')
    #end the game
    elif i == 10:
        print('Game over!. The number was {}'.format(secretNumber))
        break
