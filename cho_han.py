import random, sys
from importlib.resources.simple import TraversableReader

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5:'GO', 6:'ROKU'}

print('''Cho-han by AL Sweigart, 

In this traditional Japanese dice game, two dice are rolled.
The player must guess if the dice total to an even (cho) or odd (han) number.''')
attempts = 0
while True:
    print('How much money do you have? ')
    response = input('> ')
    if response.isdecimal():
        myMoney = int(response)
        break

    attempts += 1
    print('Only real money man!')

    if attempts >= 3:
        print('Come back when you have money!')
        sys.exit(1)

while True:
    print('You have', myMoney, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('> ')
        if pot.upper() == 'QUIT':
            print('Thank you for playing!')
            sys.exit(1)
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > myMoney:
            print('You do not have enough money.')
        else:
            pot = int(pot)
            break

    #roll the dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the dice')
    print(' CHO (even) or HAN (odd)?')

    while True:
        bet = input('> ')
        if bet != 'CHO' and bet != 'HAN':
            print('either CHO or HAN only')
            continue
        else:
            break

    #reveal the dice results
    print(' ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('     ', dice1, '     ', dice2)

    #determine if the player won:
    rollIsEven = (dice1+dice2)%2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    if playerWon:
        print('You won!', pot, 'mon')
        myMoney = myMoney + pot
        print('The house collects a', pot // 10, 'mon fee.')
        myMoney = myMoney - (pot // 10)
    else:
        myMoney = myMoney - pot
        print('You lost! ', myMoney, 'remaining')

    if myMoney == 0:
        print('You are broke, go find more money!')
        sys.exit(1)


